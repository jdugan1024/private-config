==============
Private Config
==============

This is a simple package for managing a collection of config options in a file
rather than in a script. It is intended to be used to keep private data out of
Django config files.

Here is an example::

    from private_config import PrivateConfig

    private_settings = PrivateConfig("/sites/private.cfg", 
                                     section="my-settings")

    print private_settings.api_key

The contents of `/sites/private.cfg` should be in the format understood by
ConfigParser. 
