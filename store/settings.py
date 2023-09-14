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
SECRET_KEY = 'django-insecure-l!o6w)_ggfaew5v#n_ao3d(@k6yd1h%l!@5*$4(06anf%-&%m3'  # Обеспечивает целостность передачи данных между серверами и клиентами

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # Расположение сайта по данному домену '*' - на любом домене проект будет доступен

DOMAIN_NAME = 'http://localhost:8000'  # Устанавливаем имя домена

# Application definition - установленные приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # django-allauth
    'debug_toolbar',  # django-debug-toolbar

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',

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
    "debug_toolbar.middleware.DebugToolbarMiddleware",
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
                'products.context_processors.baskets',  # Подключение своего контекстного процессора
            ],
        },
    },
]

# Расположение данного файла, для деплоя нашего проекта на продакшен
WSGI_APPLICATION = 'store.wsgi.application'

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store_db',
        'USER': 'store_username',
        'PASSWORD': 'store_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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

# Users - мы должны глобально переопределяем модель с которой мы будем работать для пользователей, так как расширяем данную модель.
AUTH_USER_MODEL = 'users.User'  # 'users.User' - название приложения, название модели
LOGIN_URL = '/users/login/'  # глобальные настроки для авторизации пользователя, что бы не прописывать в декораторе login_required. Перенаправляет на страницу незарегистрированного пользователя
LOGIN_REDIRECT_URL = '/'  # для перенаправления на главную страницу при авторизации
LOGOUT_REDIRECT_URL = '/'  # для перенаправления на главную страницу при выходе из аккаунта

# Sending email
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'stas101.VIP@yandex.ru'
# EMAIL_HOST_PASSWORD = '5464132123VATO100965'
# EMAIL_USE_SSL = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Подключение django-allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1  # django-allauth с которым сайтом будет работать

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [   # Какой scope берется
            'user',  # Пользователь
            # 'repo',  # Репозиторий
            # 'read:org',  # Данные на чтение организаций если есть у пользователя
        ],
    }
}
