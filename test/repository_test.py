import os
from os import path as p
import uuid
import json
import tempfile as t
from cleaner import repository

under_test = repository.Repository('test_resources/test_registry/', 'repository', 'images')

def assert_both_ways(expected, actual):
    for e in expected:
        assert e in actual

    for a in actual:
        assert a in expected
            

def test_repository_tagfiles():
    expected = ['test_resources/test_registry/repository/dr_clean/bar/tag_1',
                'test_resources/test_registry/repository/dr_clean/bar/tag_2',
                'test_resources/test_registry/repository/dr_clean/bar/tag_3',
                'test_resources/test_registry/repository/dr_clean/foo/tag_1',
                'test_resources/test_registry/repository/dr_clean/foo/tag_2',
                'test_resources/test_registry/repository/dr_clean/foo/tag_3']
    actual = under_test.tagfiles()

    assert_both_ways(expected, actual)
        

def test_repository_referenced_images():
    expected = {u'7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                u'ffff2732b9f49d2dbdd24545446398242d9e380dd615c4ddb61eadd4aa88ac02'}

    actual = under_test.referenced_images()

    assert actual == expected
    

def test_repository_tagged_images():
    expected = ['7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef']

    actual = list(under_test.tagged_images())

    assert_both_ways(expected, actual)
        

def test_repository_all_images():
    expected = ['7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef',
                'ffd06b1ded5fc51266eb26ab8592df609295b69a5057f11a6aa00e7c1efceb9b',
                'ffff2732b9f49d2dbdd24545446398242d9e380dd615c4ddb61eadd4aa88ac02']

    actual = under_test.all_images()

    assert_both_ways(expected, actual)
    
def test_repository_validate():
    result = under_test.validate()
    assert result == set()


def test_repository_unused_images():
    expected = ['ffd06b1ded5fc51266eb26ab8592df609295b69a5057f11a6aa00e7c1efceb9b']

    actual = under_test.unused_images()

    assert_both_ways(expected, actual)

def test_repository_get_size():
    image_id = '7f55f4c9f6942af8bc2fb123de04a7296b78536daeca5670e16893b0d0ca67ef'

    expected = 136
    actual = under_test.get_size(image_id)

    assert expected == actual, actual

    
