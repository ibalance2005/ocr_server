from os import environ as ENV
import os.path as P


def resource_path(name):
    return P.join(APP_ROOT, name)


APP_ROOT = P.dirname(P.dirname(P.realpath(__file__))).replace('\\', '/')


API_URL_PREFIX = '/api'