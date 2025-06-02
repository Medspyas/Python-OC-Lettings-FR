



SECRET_KEY = "clef_secrète_pour_la_doc"


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "oc_lettings_site",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}