"""
Django settings for OMS project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*x9a#nt!9@+4n^nf-u-_heg_t^dujr+(a5c$owi=ex_j#s+i+1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'dashboard',
    'departments',
    'oms_config',
    'dbs_mysql',
    'repository',
    'assets',
    'saltstack',
    'dbs_redis',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'OMS.urls'

WSGI_APPLICATION = 'OMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oms',
        'USER': 'root',
        'PASSWORD': 'centos',
        # 'HOST': '192.168.0.54',
        'HOST': '192.168.0.67',
        'PORT': 3306,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DEFAULT_CHARSET = 'UTF-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
)

AUTH_USER_MODEL = 'accounts.User'

SALT_FILES_ROOT = '/srv/salt/'

salt_api_url = 'http://127.0.0.1:8000/'
salt_api_user = 'admin'
salt_api_password = 'admin'


DESTINATION = []
SOURCE = []
MASTER_IP = '192.168.0.31'

GENERATE_URL = "salt://generate/"
CONF_URL = "salt://config"
SCRIPT_URL = "salt://script"


war_data_git_url = 'xxx'
web_base_git_url = 'xxx'
web_login_git_url = 'xxx'