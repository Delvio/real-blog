from myblog.settings.base import *  # noqa
from myblog.settings.base import env, ROOT_DIR
import os

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env("DJANGO_DEBUG")
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="You will not get me that easy",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}
}


# Email Settings

EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("DJANGO_EMAIL_PORT")
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS")
