from pathlib import Path

# ✅ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent


# ✅ Secret Key
SECRET_KEY = 'django-insecure-avocado-ml'

# ✅ Debug Mode
DEBUG = True

# ✅ Allowed Hosts
ALLOWED_HOSTS = []


# ✅ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your App
    'prediction',
]


# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


# ✅ Root URL Configuration
ROOT_URLCONF = 'avocado_project.urls'


# ✅ Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Templates folder location
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ✅ WSGI Application
WSGI_APPLICATION = 'avocado_project.wsgi.application'


# ✅ Database Configuration (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ✅ Language & Timezone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ======================================================
# ✅ STATIC FILES SETTINGS (IMPORTANT FOR BACKGROUND IMAGE)
# ======================================================

# URL used to access static files
STATIC_URL = '/static/'

# ✅ Tell Django where your static folder exists
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# (Optional for deployment)
STATIC_ROOT = BASE_DIR / "staticfiles"


# ======================================================
# ✅ Default Auto Field
# ======================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'