#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from main.settings import *

DEVELOPMENT = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

INSTALLED_APPS += (
    'debug_toolbar',
    )

