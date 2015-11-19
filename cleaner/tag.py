import os

class Tag(object):
    def __init__(self, tagfile_path):
        self.path = tagfile_path        

    @property
    def fname(self):
        if not hasattr(self, '_name'):
            _, name = os.path.split(self.path)
            self._name = name
        return self._name

    @property 
    def tag(self):
        return self.fname[4:] # strip leading tag_

    @property
    def mtime(self):
        if not hasattr(self, '_mtime'):
            self._mtime = os.stat(self.path).st_mtime
        return self._mtime

    @property
    def environment(self):
        is_deploy_tag = self.fname.startswith('tag_deploy_')
        return self.fname.split('_')[2] if is_deploy_tag else None

    @property
    def image(self):
        if not hasattr(self, '_image'):
            with open(self.path) as tf:
                self._image = tf.read()
        return self._image

    def __cmp__(self, other):
        return self.mtime - other.mtime
