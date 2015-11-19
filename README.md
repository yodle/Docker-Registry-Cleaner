** Docker Registry Cleaner Tools **

Current docker registries don't have great tools for cleanup. This fills the gap before it fills your disk.

# Installing

`pip install docker-registry-cleaner`

You will need to change the credentials.py file to have the correct username and password for your docker registry.

# Warning

This was developed against our docker repository. If your registry is different, it may cause problems. Please back up your registry and use scrub rather than purge until you are confident it works for your setup.

# Usage

Set up a cron job to run the script at whatever interval is best for your repository.

You may want to untag old images before purging

    ./dr_clean untag $REPOSITORY_HOME
    ./dr_clean purge $REPOSITORY_HOME


If you are using safe deletes, then you can also restore with

    ./dr_clean restore $REPOSITORY_HOME

This might be wise if you have frequent enough pushes. There is a race condition where an image may be pushed, but the reference is not written to disk yet, and it will be picked up for deletion. This won't happen if your $KEEP window is long enough though.

# Contributing

Pull requests are welcome! All tests must pass and be pep8 compliant. .

# License

Apache 2 Licensed.
