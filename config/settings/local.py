from datetime import timedelta

from celery.schedules import crontab

from .base import *  # noqa
from .base import env

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

CELERY_BROKER_URL = env.str("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = env.str("CELERY_BACKEND", "redis://127.0.0.1:6379/0")

CELERY_BEAT_SCHEDULE = {
    "Check Depug": {
        "task": "apps.utils.tasks.check_depug",
        "schedule": crontab(minute="*/5"),
    },
}

ADMIN_URL = env.str("ADMIN_URL", default="admin/")
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT", "Bearer"),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
}
