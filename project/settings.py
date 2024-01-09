import os
from django.contrib.messages import constants as messages
import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool(("DEBUG"), default=True)


ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    "https://team.soulnbody.net,localhost,164.90.182.196,team.soulnbody.net,*",
).split(",")
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"
CORS_ALLOWED_ORIGINS = [
    "http://team.soulnbody.net",
    "164.90.182.196",
]
CSRF_TRUSTED_ORIGINS = [
    "http://team.soulnbody.net",
    "http://164.90.182.196",
]

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Application definition

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Soul Body Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Soul Body",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Soul Body",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": None,
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to Soul Body",
    # Copyright on the footer
    "copyright": "Soul Body 2023",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
}
INSTALLED_APPS = [
    "daphne",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "crispy_forms",
    "crispy_bootstrap5",
    "widget_tweaks",
    "django_htmx",
    "django.contrib.humanize",
    "django_celery_beat",
    "sweetify",
    "django_cleanup.apps.CleanupConfig",
    "errorpages",
    "posts",
    "members",
    "crm",
    "products",
    "notification",
]


SWEETIFY_SWEETALERT_LIBRARY = "sweetalert2"
"""CELERY_BEAT_SCHEDULE = {
    "scheduled_task": {
        "task": "posts.tasks.Schedule_Posts",
        "schedule": 3.0,
    },

}"""

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DataBaseChose = env("Datalocal")

WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"

if DataBaseChose == "True":
    CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

else:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [
                    "redis://default:toEMVv84QMIbWM5NUlOO@containers-us-west-146.railway.app:5795"
                ],
            },
        },
    }


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

db_path = os.path.join(str(BASE_DIR), "db.sqlite3")

if DataBaseChose == "True":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": db_path,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("PGDATABASE"),
            "USER": env("PGUSER"),
            "PASSWORD": env("PGPASSWORD"),
            "HOST": env("PGHOST"),
            "PORT": "",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"
CELERY_TIMEZONE = "UTC"
USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("ar", _("Arabic")),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

STATIC_URL = "/static/"

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(str(BASE_DIR), "staticfiles")

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_PASS")

# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
# AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
# AWS_QUERYSTRING_EXPIRE = 120
# AWS_S3_CUSTOM_DOMAIN = "d6prksi5n1o97.cloudfront.net"
"""AWS_CLOUDFRONT_KEY = (
    env.str("AWS_CLOUDFRONT_KEY", multiline=True).encode("ascii").strip()
)"""
# AWS_CLOUDFRONT_KEY_ID = env.str("AWS_CLOUDFRONT_KEY_ID").strip()
