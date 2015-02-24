import ConfigParser

class PrivateConfigKeyError(Exception):
    pass

class PrivateConfig(object):
    """Simple class for storing private items.

    This is primarily intended to be used with Django to keep items that
    are better kept outside settings.py.
    """

    def __init__(self, filename, section="main", type_map={}):
        self.filename = filename
        self.section = section
        self.type_map = type_map
        self._data = {}

        cfg = ConfigParser.ConfigParser()
        cfg.optionxform = str
        cfg.read(filename)

        for k, v in cfg.items(section):
            if k in self.type_map:
                v = self.type_map[k](v)

            self._data[k] = v

    def __getattr__(self, name):
        try:
            return self._data[name]
        except KeyError, e:
            raise PrivateConfigKeyError("unable to find entry for %s in %s, section [%s]" % (name, self.filename, self.section))


    def __contains__(self, name):
        return name in self._data
