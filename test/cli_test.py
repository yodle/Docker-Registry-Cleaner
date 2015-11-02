import cleaner

def test_parameters():
    keys = cleaner.commands.keys()
    for k in ['untag', 'images', 'scrub', 'validate']:
        assert k in keys

def test_bad_parameter_is_error():
    try:
        cleaner.run('not-a-command')
        assert False
    except ValueError as v:
        assert True
        
def test_good_parameter_is_True():
    assert cleaner.run('untag')
