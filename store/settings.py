"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Полный путь ведущий до проекта store


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l!o6w)_ggfaew5v#n_ao3d(@k6yd1h%l!@5*$4(06anf%-&%m3' # Обеспечивает целостность передачи данных между серверами и клиентами

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # Расположение сайта по данному домену '*' - на любом домене проект будет доступен


# Application definition - установленные приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products.apps.ProductsConfig',
    'users.apps.UsersConfig'
]
# Промежуточные слои
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # отвечает за безопасность
    'django.contrib.sessions.middleware.SessionMiddleware',  # за проброску сессий для пользователей
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Защиту от отак Csrf токен
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аунтификацию добавляет и т.д
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Там где распологаются наши URL адреса
ROOT_URLCONF = 'store.urls'

# Отвечает за отображение шаблонов и работу с шаблонами
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Для того что бы шаблон оживился и выполнял какие-то методы, необходимо использовать BACKEND - движок для шаблонов.
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # С мощью данной строчки можно обращаться к пользователю user в template теге
                'django.contrib.messages.context_processors.messages',  # С мощью данной строчки можно обращаться к пользователю user в template теге
            ],
        },
    },
]

# Расположение данного файла, для деплоя нашего проекта на продакшен
WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation - валидация для паролей
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Указываем путь до папки статик

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'