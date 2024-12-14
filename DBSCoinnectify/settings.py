from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

INSTANCE_DIR = BASE_DIR / 'instance'

if not INSTANCE_DIR.exists():
    INSTANCE_DIR.mkdir()

SECRET_KEY = 'po0172$69b@78ps4v^uhfxu6q--8ko7kpp7rbz420s_3w#sir%'

DEBUG = false

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/transactions/report'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_beat',

    'accounts',
    'core',
    'transactions',
    'crypto',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DBSCoinnectify.urls'
AUTH_USER_MODEL = 'accounts.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DBSCoinnectify.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': INSTANCE_DIR / 'DBSCoinnectifyDB.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# Add this line to include static files from the root `static` directory
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # This points to the root static directory
]

ACCOUNT_NUMBER_START_FROM = 1000000000
MINIMUM_DEPOSIT_AMOUNT = 10
MINIMUM_WITHDRAWAL_AMOUNT = 10

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
