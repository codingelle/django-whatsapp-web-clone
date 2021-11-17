from .settings import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PSQL_NAME'),
        'USER': os.getenv('PSQL_USER'),
        'PASSWORD': os.getenv('PSQL_PASS'),
        'HOST': os.getenv('PSQL_HOST'),
        'PORT': os.getenv('PSQL_PORT'),
    }
}

TORTOISE_INIT = {
    "db_url": f"postgres://{os.getenv('PSQL_USER')}:{os.getenv('PSQL_PASS')}@{os.getenv('PSQL_HOST')}:{os.getenv('PSQL_PORT')}/{os.getenv('PSQL_NAME')}",
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