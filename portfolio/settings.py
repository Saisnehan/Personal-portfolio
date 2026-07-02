from pathlib import Path
import os
from dotenv import load_dotenv

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------
# SECURITY
# --------------------------------------------------

SECRET_KEY = "django-insecure-)=c14dk$z1rx=4oln9l&hz4cg_(t8xdpug-vd95=0+dnyb)8#@"

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
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

USE_POSTGRES = os.getenv("USE_POSTGRES", "False") == "True"

if USE_POSTGRES:

    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "CONN_MAX_AGE": 600,
    }
}
else:

    DATABASES = {

        "default":{

            "ENGINE":"django.db.backends.sqlite3",

            "NAME":BASE_DIR/"db.sqlite3",

        }

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

STATICFILES_DIRS = [

    BASE_DIR/"main/static",

]

STATIC_ROOT = BASE_DIR/"staticfiles"

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