from cleaner import docker_project

under_test = docker_project.DockerProject("some/path")

docker_project.os.listdir = lambda d: ["tag_file1", "tag_file2"]

def test_name_and_path_are_parsed_correctly():
    assert under_test.path == "some/path"
    assert under_test.name == "path"

def test_tagfiles_are_memoized():
    assert not hasattr(under_test, "_tagfiles")
    assert under_test.tagfiles == ["tag_file1", "tag_file2"]
    assert hasattr(under_test, "_tagfiles")
