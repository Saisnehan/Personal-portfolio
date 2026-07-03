from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------
# SECURITY
# --------------------------------------------------

SECRET_KEY = "django-insecure-)=c14dk$z1rx=4oln9l&hz4cg_(t8xdpug-vd95=0+dnyb)8#@"

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    ".railway.app",
    "127.0.0.1",
    "localhost",
]
CSRF_TRUSTED_ORIGINS = [
    "https://personal-portfolio-production-3dcc.up.railway.app",
]
# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "main",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",

]

SITE_ID = 2

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    'whitenoise.middleware.WhiteNoiseMiddleware',

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

# --------------------------------------------------
# URLS
# --------------------------------------------------

ROOT_URLCONF = "portfolio.urls"

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------

TEMPLATES = [

    {
        "BACKEND":"django.template.backends.django.DjangoTemplates",

        "DIRS":[BASE_DIR/"main/templates"],

        "APP_DIRS":True,

        "OPTIONS":{

            "context_processors":[

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]

# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = "portfolio.wsgi.application"

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv(
            "DATABASE_URL",
            f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
        ),
        conn_max_age=600,
    )
}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":"django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":"django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":"django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "main/static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------

AUTHENTICATION_BACKENDS = [

    "django.contrib.auth.backends.ModelBackend",

    "allauth.account.auth_backends.AuthenticationBackend",

]

LOGIN_URL = "/accounts/google/login/"

LOGIN_REDIRECT_URL = "/download-resume/"

LOGOUT_REDIRECT_URL = "/"

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_PROVIDERS = {

    "google":{

        "SCOPE":[

            "profile",

            "email",

        ],

        "AUTH_PARAMS":{

            "access_type":"online",

        },

    }

}