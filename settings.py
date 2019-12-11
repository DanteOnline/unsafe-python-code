"""
Уязвимости в коде в django проекте
"""

# Явно указаны логин и пароль от почты
from django.views.decorators.csrf import csrf_exempt

EMAIL_HOST_USER = 'my@my.com'
EMAIL_HOST_PASSWORD = 'thisismypass'

# Выключен csrf
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Вот этот закоменчен или удалет
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# Где то в коде csrf выключен локально, используется декоратор csrf_exempt
@csrf_exempt
def my_view(request):
    pass
