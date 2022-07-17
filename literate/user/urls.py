from atexit import register
from . import views as user_view
from bot import views as bot_view
from django.urls import path, include
urlpatterns = [
    path('', user_view.index),
    path('bot', bot_view.check_command),
    path('signup', user_view.signup),
    path('signin', user_view.signin),
    path('auth', user_view.auth),
    path('register', user_view.register)
]
