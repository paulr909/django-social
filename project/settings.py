from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "b4&ixp%mylp+$$6y&pdsq!z9v@68c8dynlqgk#t)9vm!%9-54q"

DEBUG = True

ALLOWED_HOSTS = ["django-social.com", "localhost", "127.0.0.1", "e2bddbbf.ngrok.io"]

INSTALLED_APPS = [
    "account.apps.AccountConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "images.apps.ImagesConfig",
    "sorl.thumbnail",
    "actions.apps.ActionsConfig",
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

LOGIN_REDIRECT_URL = "dashboard"
LOGIN_URL = "login"
LOGOUT_URL = "logout"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "account.authentication.EmailAuthBackend",
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.twitter.TwitterOAuth",
    "social_core.backends.google.GoogleOAuth2",
]

# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = ""  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = ""  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]

SOCIAL_AUTH_TWITTER_KEY = ""  # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = ""  # Twitter Consumer Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ""  # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ""  # Google Consumer Secret

from django.urls import reverse_lazy

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda u: reverse_lazy("user_detail", args=[u.username])
}

# Redis settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
