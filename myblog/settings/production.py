from myblog.settings.base import *  # noqa
from myblog.settings.base import env


SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS")

DATABASES["default"] = env.db("DATABASE_URL")


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
