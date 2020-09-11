from myblog.settings.base import *  # noqa
from myblog.settings.base import env


SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS")

DATABASES["default"] = env.db("DATABASE_URL")
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int(  # noqa F405
    "CONN_MAX_AGE", default=60
)

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)


EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("DJANGO_EMAIL_PORT")
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS")
