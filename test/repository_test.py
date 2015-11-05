import os
from os import path as p
import uuid
import json
import tempfile as t
from cleaner import repository

def test_repository_tagfiles():
    under_test = repository.Repository('test_resources/test_registry/', 'repository', 'images')
    expected = ['test_resources/test_registry/repository/dr_clean/bar/tag_1',
                'test_resources/test_registry/repository/dr_clean/bar/tag_2',
                'test_resources/test_registry/repository/dr_clean/bar/tag_3',
                'test_resources/test_registry/repository/dr_clean/foo/tag_1',
                'test_resources/test_registry/repository/dr_clean/foo/tag_2',
                'test_resources/test_registry/repository/dr_clean/foo/tag_3']
    actual = under_test.tagfiles()

    for e in expected:
        assert e in actual

def test_repository_referenced_images():
    under_test = repository.Repository('test_resources/test_registry/', 'repository', 'images')

    expected = {u'7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                u'ffff2732b9f49d2dbdd24545446398242d9e380dd615c4ddb61eadd4aa88ac02'}

    actual = under_test.referenced_images()

    assert actual == expected

def test_repository_tagged_images():
    under_test = repository.Repository('test_resources/test_registry/', 'repository', 'images')

    expected = ['7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef']

    actual = list(under_test.tagged_images())

    for e in expected:
        assert e in actual

    for a in actual:
        assert a in expected

def test_repository_all_images():
    under_test = repository.Repository('test_resources/test_registry/', 'repository', 'images')
    
    expected = ['7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                'ffd06b1ded5fc51266eb26ab8592df609295b69a5057f11a6aa00e7c1efceb9b',
                'ffff2732b9f49d2dbdd24545446398242d9e380dd615c4ddb61eadd4aa88ac02']

    actual = under_test.all_images()

    for e in expected:
        assert e in actual

    for a in actual:
        assert a in expected
