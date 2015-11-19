"""
Docker repository on-disk model
Based on code from https://github.com/docker/docker-registry by Docker
"""

import json
import logging
import os
import shutil
import tempfile

from os.path import join, basename, isfile

from credentials import username, password


class Repository(object):
    def __init__(self, root_path, repositories='repositories', images='images'):
        self.root_path = root_path
        self.repositories = repositories
        self.images = images

    def validate(self):
        """Returns the set of referenced images not found in the repository. 
           An empty set means the registry is in a valid state"""
        
        referenced_images = self.referenced_images()
        all_images = set(self.all_images())
        
        diff = referenced_images - all_images
        return diff

    def report(self):
        def get_size(img_id):
            try:
                return self.get_size(img_id)
            except:
                return -1

        report = {i: get_size(i) for i in self.unused_images()}
        return report


    def untag(self):
        pass

    def unused_images(self):
        return set(self.all_images()) - self.referenced_images()
        
    def tagged_images(self):
        for tf in self.tagfiles():
            try:
                with open(tf, mode='r') as f:
                    result = f.read().strip()
                    yield result
            except (IOError, OSError) as e:
                print(e)
                continue

    def all_images(self):
        path = join(self.root_path, self.images)
        return os.listdir(path)

    def referenced_images(self):
        """Returns a set of referenced image ids"""
        return {a for i in self.tagged_images()
                  for a in self.ancestry(i)}

    def ancestry(self, image_id):
        p = join(self.root_path, self.images, image_id, "ancestry")
        if not isfile(p):
            return iter([])
        with open(p, mode='r') as f:
            data = f.read()
            result = iter(json.loads(data))
            return result
        
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

    def get_size(self, image_id):
        path = join(self.root_path, self.images, image_id)
        return os.path.getsize(path)

    def remove(self, image_id):
        path = join(self.root_path, self.images, image_id)
        tmp = tempfile.mkdtemp(prefix='unused-images')
        print("Moving %s to %s" % (path, tmp))
        shutil.move(path, tmp)        
        
    def revert(self, source):
        image_path = join(self.root_path, self.images)
        for dirs in os.listdir(source):
            path = join(source, dirs)
            try:
                print("Moving %s to %s" % (path, image_path))
                shutil.move(path, image_path)
            except shutil.Error as e:
                print(e)
                continue
