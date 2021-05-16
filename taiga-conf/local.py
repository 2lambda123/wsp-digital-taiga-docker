# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
#
# Importing docker provides common settings, see:
# https://github.com/benhutchins/docker-taiga/blob/master/docker-settings.py
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .docker import *

import os

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False

## Slack
# https://github.com/taigaio/taiga-contrib-slack
# INSTALLED_APPS += ["taiga_contrib_slack"]

## LDAP
# see https://github.com/ensky/taiga-contrib-ldap-auth
# INSTALLED_APPS += ["taiga_contrib_ldap_auth"]

## For additional configuration options, look at:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example

DEFAULT_FROM_EMAIL = 'admin+taiga@wspdigital.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.ap-southeast-2.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
