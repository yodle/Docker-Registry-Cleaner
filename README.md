**Docker Registry Cleaner Tools**

At [Yodle](http://www.yodle.com/), we started using Docker with a privately hosted [Docker Registry](https://github.com/docker/docker-registry). This was great until we discovered that the registry had no tools to cleanup old, unused images! Our disks began to fill up, so this was created to fill the gap.

This cleaner is designed to work with the v1 Registry provided by Docker. It has not been tested against the [Registry v2](https://github.com/docker/distribution), which may have different assumptions. We will gladly accept pull requests to add support for this (see Contributing below).

This tool is best used as a scheduled task, to periodicly remove cruft from your registry on disk. It is also advisible to untag old images as well. Tagged images are always referenced, so there may be cruft that this cleaner will not notice. Untagging as a feature will be included in this project as a plugin.

# Installing

To use this cleaner, clone the repository and run `python cleaner` from the project root

Coming soon: `pip install docker-registry-cleaner`


# Warning

This was developed against our docker repository. If your registry is different, it may cause problems. Please back up your registry and use scrub rather than purge until you are confident it works for your setup. In particular, this tool assumes you are storing your images directly on disk. It has not been designed to work with other storage drivers yet.

# Usage

In order to authenticate against your registry, you need to set the following environment variables:

`registry_username` and `registry_password`

    usage: cleaner [-h] [--hostname [HOSTNAME [HOSTNAME ...]]] [--path PATH]
               repository command

    positional arguments:
      repository            the repository path
      command               untag, validate, report, scrub, revert

    optional arguments:
      -h, --help            show this help message and exit
      --hostname [HOSTNAME [HOSTNAME ...]]
                            the registry hostname. Required for untag
      --path PATH           path to tmp directory to restore



You may want to untag old images before purging

    ./dr_clean untag $REPOSITORY_HOME
    ./dr_clean purge $REPOSITORY_HOME


If you are using safe deletes, then you can also restore with

    ./dr_clean restore $REPOSITORY_HOME

This might be wise if you have frequent enough pushes. There is a race condition where an image may be pushed, but the reference is not written to disk yet, and it will be picked up for deletion. This won't happen if your $KEEP window is long enough though.

# Contributing

Pull requests are welcome! All tests must pass and be pep8 compliant.

Tests are run by executing ```nosetests``` in the root of the project.

Style is checked by running ```pylint``` in the root of the project.

# License

Apache 2 Licensed.
