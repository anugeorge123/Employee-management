import dj_database_url

from decouple import config

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

