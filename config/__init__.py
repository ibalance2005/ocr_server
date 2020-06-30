from os import environ


PROFILE = environ.get('PROFILE', 'test')

if PROFILE == 'prod':
    from config.prod import *
else:
    from config.test import *