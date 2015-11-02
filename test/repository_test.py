import os
from os import path as p
import uuid
import json
import tempfile as t
from cleaner import repository

def construct_repository():
    """ Construct a mock repository on disk
    /root
    \____repo_path
    |    \____namespace
    |         \____repo
    \____images    \____[tags]
                   \____[data]
    """
    rootpath = t.mkdtemp()
    repo_path = t.mkdtemp(dir=rootpath, prefix="repo")
    img_path = t.mkdtemp(dir=rootpath, prefix="img")
    img = t.mkdtemp(dir=img_path)    
    namespace = t.mkdtemp(dir=repo_path, prefix="ns")
    repo_data = t.mkdtemp(dir=namespace, prefix="data")
    tags = [t.mkstemp(dir=repo_data, prefix='tag_')[1] for _ in range(10)]
    data = [t.mkstemp(dir=repo_data, prefix='data_')[1] for _ in range(10)]

    for tg in tags:
        with open(tg, 'wb') as f:
            f.write(p.basename(img))

    with open(img + "/ancestry", 'w') as g:
        g.write(json.dumps([p.basename(img)]))

    return repository.Repository(rootpath,
                                 repositories=p.basename(repo_path),
                                 images=p.basename(img_path)), tags, img

def test_tagged_images():
    store, tags, _ = construct_repository()
    result = [r for r in store.tagged_images()]
    expected = []
    for t in tags:
        with open(t) as f:
            expected.append(f.read())
    assert len(result) == len(expected) == 10

    for r in result:
        assert r in expected

def test_referenced_images():
    store, _, img = construct_repository()
    result = next(store.ancestry(img))
    assert result == p.basename(img), (result, img)
    
