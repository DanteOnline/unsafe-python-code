"""
Уязвимости в коде в django проекте
"""

# Явно указаны логин и пароль от почты - Содержит уязвимость
from django.views.decorators.csrf import csrf_exempt

EMAIL_HOST_USER = 'my@my.com'
EMAIL_HOST_PASSWORD = 'thisismypass'

# Выключен csrf
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Вот этот закоменчен или удалет - потенциально небезопасно
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# Где то в коде csrf выключен локально, используется декоратор csrf_exempt, Потенциально небезопасно
@csrf_exempt
def my_view(request):
    pass
