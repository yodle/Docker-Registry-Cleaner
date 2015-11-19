from cleaner import app
import sys

def test_parse_args():
    sys.argv = ['cleaner', 'repo-location', 'test']
    result = app.parse_args()

    assert result.repository == 'repo-location'
    assert result.command == 'test'
