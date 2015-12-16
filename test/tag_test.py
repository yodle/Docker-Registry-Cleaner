import tempfile
from cleaner import tag

t = tempfile.NamedTemporaryFile(prefix="tag_", dir="/tmp")
under_test = tag.Tag(t.name)

def test_memoization():
    assert not hasattr(under_test, '_name')
    expected_name = t.name.split('/')[-1][4:]
    assert expected_name == under_test.tag
    assert hasattr(under_test, '_name')

    assert not hasattr(under_test, '_mtime')
    under_test.mtime
    assert hasattr(under_test, '_mtime')

    assert not hasattr(under_test, '_image')
    under_test.image
    assert hasattr(under_test, '_image')
