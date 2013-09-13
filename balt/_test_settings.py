from balt.settings import *

DEBUG = False

PASSWORD_HASHERS = (
    # Fast plz
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'balt-test-unique-snowflake'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] [%(asctime)s] [%(name)s]: %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'tutorials': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'core.tasks': {
            'handlers': ['console'],
            'propagate': False,
            'level':'DEBUG',
        },
    } 
}

NOSE_ARGS = [
    '--with-coverage',
    '--verbose',
    '--logging-clear-handlers',
    '--cover-package=tutorials,balt',
]

TESTING = True

# Developers should always have a _local_tests.py file.  Copy it from _local_tests.py.example and customize.
# If you need to locally override things (like NOSE_ARGS), add them to _local_tests.py
try:
    from balt._local_tests import *
except ImportError, e:
    print u"FYI: You have no balt/_local_tests.py, but you should!"
    pass

