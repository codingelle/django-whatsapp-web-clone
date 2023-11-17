from .settings import *
from dotenv import load_dotenv

load_dotenv('.env.production')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DEBUG = False

STATIC_URL = "/django-whatsapp-clone/static/"
MEDIA_URL = "/django-whatsapp-clone/media/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRESQL_DATABASE'),
        'USER': os.getenv('POSTGRESQL_USER'),
        'PASSWORD': os.getenv('POSTGRESQL_PASSWORD'),
        'HOST': os.getenv('POSTGRESQL_HOST'),
        'PORT': os.getenv('POSTGRESQL_PORT'),
    }
}

TORTOISE_INIT = {
    "db_url": f"postgres://{os.getenv('POSTGRESQL_USER')}:{os.getenv('POSTGRESQL_PASSWORD')}@{os.getenv('POSTGRESQL_HOST')}:{os.getenv('POSTGRESQL_PORT')}/{os.getenv('POSTGRESQL_DATABASE')}",
    "modules" : {
        "models": ["chat.tortoise_models"]
     }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))],
        },
    },
}

WS_URL = "wss://demo.josnin.dev/django-whatsapp-clone/ws/chat"