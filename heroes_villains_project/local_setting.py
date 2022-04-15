# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bmgod$8z@w9i!a+#i8&8*8grkz@d_f58cj&!1_t7_j(l&$@(x$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
