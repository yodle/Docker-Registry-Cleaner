"""
Docker repository on-disk model
Based on code from https://github.com/docker/docker-registry by Docker
"""

import os
from os.path import join, basename
import json

def tagged_images(store):
    for tf in store.tagfiles():
        try:
            with open(tf, mode='rb') as f:
                yield f.read()
        except Exception:
            continue
        

class Repository(object):
    def __init__(self, root_path, repositories, images):
        self.root_path = root_path
        self.repositories = repositories
        self.images = images

    def tagged_images(self):
        for tf in self.tagfiles():
            try:
                with open(tf, mode='rb') as f:
                    yield f.read()
            except (IOError, OSError) as e: 
                continue

    def ancestry(self, image_id):
        p = join(self.root_path, self.images, image_id, "ancestry")
        with open(p, mode='rb') as f:
            data = f.read()
            return iter(json.loads(data))
        
    def tagfiles(self):
        """Returns a list of all tagfiles in the repository"""
        # Functional directory walking!
        base = join(self.root_path, self.repositories)
        namespaces = [join(base, d) for d in os.listdir(base)]
        repos = {ns: os.listdir(ns) for ns in namespaces}
        tag_dirs = [os.path.join(r, t) for r in repos
                                       for t in repos[r]]
        tags = [os.path.join(d, t) for d in tag_dirs
                                   for t in os.listdir(d)]

        return filter(lambda t: basename(t).startswith('tag_'), tags)
    
