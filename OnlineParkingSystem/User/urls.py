from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'registration/', views.Registration, name="registration"),
    url(r'login/', views.Login, name="login"),
    url(r'', views.Login, name="login"),
]