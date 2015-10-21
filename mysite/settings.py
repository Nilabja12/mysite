import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o&d%lngs4h*!svr$txifgqsyxa3%jh%49f-vo)pr!-v^*0t^pn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='rayn1209@gmail.com'
EMAIL_HOST_PASSWORD='neel_1990'
EMAIL_PORT=587
EMAIL_USE_TLS=True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration',
    'crispy_forms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'mysite',
    }
}


TEMPLATE_DIRS= (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR,'registration', 'templates'),

)


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_URL = '/media/'

STATIC_ROOT=os.path.join(BASE_DIR, "static","static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static",'my_static'),
#    '/var/www/static/',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

#AUTH_USER_MODEL = 'registration.User'
SITE_ID=u"5621b163b81534169d87d883"