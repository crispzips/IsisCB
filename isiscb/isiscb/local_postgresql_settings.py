"""
Django settings for isiscb project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from __future__ import unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

sys.path.append('..')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4z1u)a6b5l%#uf3qi$$$^s^3_*%cruf9pfk$jdgm&n2%ov11%m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#INTERNAL_IPS = ['127.0.0.1']

MIGRATION_MODULES = {
    'isisdata': 'isisdata.migrations'
}

# Application definition

INSTALLED_APPS = (
    'dal',
    'dal_select2',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'rest_framework',
    'simple_history',
    'isisdata',
    'storages',
    'haystack',
    "elasticstack",
    'oauth2_provider',
    'captcha',
    'corsheaders',
    'zotero',
    'openurl',
    'curation',
    'rules.apps.AutodiscoverRulesConfig',
    #'dj_pagination',
    #'debug_toolbar',
)

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE= [
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    #'dj_pagination.middleware.PaginationMiddleware',
]

AUTHENTICATION_BACKENDS = (
    # TODO: Remove
    #'social.backends.twitter.TwitterOAuth',
    #'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY', '')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('SOCIAL_AUTH_TWITTER_SECRET', '')

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET', '')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

FACEBOOK_APP_ID = SOCIAL_AUTH_FACEBOOK_KEY
FACEBOOK_API_SECRET = SOCIAL_AUTH_FACEBOOK_SECRET



SOCIALACCOUNT_PROVIDERS = {
    'twitter': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': SOCIAL_AUTH_TWITTER_KEY,
            'secret': SOCIAL_AUTH_TWITTER_SECRET,
            'key': ''
        }
    },
    'facebook': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': SOCIAL_AUTH_FACEBOOK_KEY,
            'secret': SOCIAL_AUTH_FACEBOOK_SECRET,
            'key': ''
        },
        'METHOD': 'oauth2',
        'fields': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
        ]
    }
}

SOCIALACCOUNT_AUTO_SIGNUP = True

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'social.apps.django_app.context_processors.backends',
#     'social.apps.django_app.context_processors.login_redirect',
# )


ROOT_URLCONF = 'isiscb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['isisdata/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                'isisdata.context_processors.social',
            ],
        },
    },
]

#WSGI_APPLICATION = 'isiscb.wsgi.application'

LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"formatters": {
		"verbose": {"format": "%(asctime)s %(levelname)s %(module)s: %(message)s"}
	},
	"handlers": {
		"app_analyzer": {
			"level": "DEBUG",
			"class": "logging.FileHandler",
			"filename": "/Users/jdamerow/UpConsulting/logs/app_analyzer.log",
			"formatter": "verbose",
		}
	},
	"loggers": {
		"app_analyzer": {"handlers": ["app_analyzer"], "level": "DEBUG", "propagate": True}
	},
}

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# from secrets import POSTGRESQL_PASSWORD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'isiscb_new',
        'USER': 'upconsulting',
        'PASSWORD': 'upconsulting',
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': '5432',
    }
}

HAYSTACK_DEFAULT_INDEX = 'default'
HAYSTACK_CONNECTIONS = {
    HAYSTACK_DEFAULT_INDEX: {
        'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': os.environ.get('ELASTIC_HOST', 'localhost:9200/'),
        'INDEX_NAME': 'haystack',
    },
}


ELASTICSEARCH_INDEX_SETTINGS = {
     "settings" : {
         "analysis" : {
             "analyzer" : {
                 "default" : {
                     "tokenizer" : "standard",
                     "filter" : ["standard", "asciifolding"]
                 }
             }
         }
     }
 }

ELASTICSEARCH_DEFAULT_ANALYZER = 'default'

CACHES = {
    #'default': {
    #    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #    'LOCATION': 'unique-snowflake',
    #},
    'default': {
        'BACKEND': "django.core.cache.backends.db.DatabaseCache",
        'LOCATION': 'db_cache_snowflake',
    },
    'search_results_cache': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'search_cache',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope', 'api': 'API scope'}
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_METADATA_CLASS': 'isisdata.metadata.CCMetadata'
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_ROOT = os.environ.get('STATIC_ROOT', '')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

AWS_HEADERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

AWS_IMPORT_BUCKET_NAME = os.environ.get('AWS_IMPORT_BUCKET_NAME')

DOMAIN = 'data.isiscb.org'
URI_PREFIX = 'http://localhost:8000/isis/'
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', False)

# try:
#     from secrets import SMTP_USER, SMTP_PASSWORD
#     EMAIL_HOST_USER = SMTP_USER
#     EMAIL_HOST_PASSWORD = SMTP_PASSWORD
# except ImportError:
EMAIL_HOST_USER = os.environ.get('SMTP_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('SMTP_PASSWORD', '')
EMAIL_HOST = os.environ.get('SMTP_HOST', 'localhost')
SMTP_EMAIL = os.environ.get('SMTP_EMAIL', 'isiscb@aplacecalledup.com')
DEFAULT_FROM_EMAIL = os.environ.get('SMTP_EMAIL', 'isiscb@aplacecalledup.com')

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FONT_SIZE = 36

LICENSE = """This work is licensed under a Creative Commons
             Attribution-NonCommercial 4.0 International License."""

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

CELERY_REDIS_HOST = os.environ.get('CELERY_REDIS_HOST', 'redis://')
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://')

CITATION_CREATION_DEFAULT_DATE = "2000-01-01T00:00:00Z"

# time till next timeline refresh in hours (720 = 30 days)
AUTHORITY_TIMELINE_REFRESH_TIME = os.environ.get('AUTHORITY_TIMELINE_REFRESH_TIME', 720)
AUTHORITY_TIMELINE_REFRESH_TIME_USER_INIT = os.environ.get('AUTHORITY_TIMELINE_REFRESH_TIME_USER_INIT', 0.25)
TIMELINE_PUBLICATION_DATE_ATTRIBUTE = os.environ.get('TIMELINE_PUBLICATION_DATE_ATTRIBUTE', "PublicationDate")
RECORD_SUBTYPE_ATTRIBUTE = os.environ.get('RECORD_SUBTYPE_ATTRIBUTE', "RecordSubType")
ACCESSED_ATTRIBUTE_NAME = os.environ.get('ACCESSED_ATTRIBUTE_NAME', "LastAccessedDate")

DOI_LINKED_DATA_NAME = os.environ.get('DOI_LINKED_DATA_NAME', "DOI")
ISBN_LINKED_DATA_NAME = os.environ.get('ISBN_LINKED_DATA_NAME', "ISBN")
URL_LINKED_DATA_NAME = os.environ.get('URL_LINKED_DATA_NAME', "URL")

JOURNAL_ABBREVIATION_ATTRIBUTE_NAME = os.environ.get('JOURNAL_ABBREVIATION_ATTRIBUTE_NAME', "JournalAbbr")
PERSON_BIRTH_DATE_ATTRIBUTE = os.environ.get('PERSON_BIRTH_DATE_ATTRIBUTE', "Birth date")
PERSON_DEATH_DATE_ATTRIBUTE = os.environ.get('PERSON_BIRTH_DATE_ATTRIBUTE', "Death date")
PERSON_BIRTH_DEATH_DATE_ATTRIBUTE = os.environ.get('PERSON_BIRTH_DATE_ATTRIBUTE', "BirthToDeathDates")

DATASET_ISISCB_NAME_PREFIX = os.environ.get('DATASET_ISISCB_NAME_PREFIX', 'Isis Bibliography of the History of Science')
DATASET_ISISCB_NAME_DISPLAY = os.environ.get('DATASET_ISISCB_NAME_DISPLAY', 'Isis Bibliography of the History of Science')
DATASET_SHOT_NAME_PREFIX = os.environ.get('DATASET_SHOT_NAME_PREFIX', 'Technology & Culture Bibliography')
DATASET_SHOT_NAME_DISPLAY = os.environ.get('DATASET_SHOT_NAME_DISPLAY', 'Technology & Culture Bibliography')

CELERY_DEFAULT_QUEUE = os.environ.get('SQS_QUEUE', 'default')
CELERY_GRAPH_TASK_QUEUE = os.environ.get('SQS_QUEUE_GRAPHS', 'graph-tasks')

CELERY_QUEUES = {
    CELERY_DEFAULT_QUEUE: {
        'exchange': CELERY_DEFAULT_QUEUE,
        'binding_key': CELERY_DEFAULT_QUEUE,
    },
    CELERY_GRAPH_TASK_QUEUE: {
        'exchange': CELERY_GRAPH_TASK_QUEUE,
        'binding_key': CELERY_GRAPH_TASK_QUEUE,
    }
}
CELERY_TASK_DEFAULT_QUEUE = CELERY_DEFAULT_QUEUE


SITE_ID = 1
ACCOUNT_FORMS = {'signup': 'isisdata.forms.UserRegistrationForm'}
ACCOUNT_EMAIL_REQUIRED = True

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_EXPORT_BUCKET_NAME = os.environ.get('AWS_EXPORT_BUCKET_NAME', '')

S3_UPLOAD_BULK_CHANGE_PATH = 's3://{}:{}@{}/'.format(AWS_ACCESS_KEY_ID,
                                AWS_SECRET_ACCESS_KEY,
                                AWS_EXPORT_BUCKET_NAME)

UPLOAD_BULK_CHANGE_PATH = os.environ.get('UPLOAD_BULK_CHANGE_PATH', S3_UPLOAD_BULK_CHANGE_PATH)

S3_BULK_CHANGE_ERROR_PATH = 's3://{}:{}@{}/'.format(AWS_ACCESS_KEY_ID,
                                AWS_SECRET_ACCESS_KEY,
                                AWS_EXPORT_BUCKET_NAME)

BULK_CHANGE_ERROR_PATH = os.environ.get('BULK_CHANGE_ERROR_PATH', S3_BULK_CHANGE_ERROR_PATH)
