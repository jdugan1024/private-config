from distutils.core import setup

setup(
    name='private-config',
    version='1.0',
    author='Jon M. Dugan',
    author_email='jdugan@x1024.net',
    description='Simple way to keep private data out of config files.',
    long_description=open("README.txt").read(),
    py_modules=['private_config'],
)
