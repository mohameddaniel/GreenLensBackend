from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login),
    path('register', views.Register),
    path('predict', views.get_consiel),
    path('history', views.get_history),
    path('profile', views.getProfile),
]
