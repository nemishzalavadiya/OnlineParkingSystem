from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'registration/', views.RegistrationView.as_view(), name="registration"),
    url(r'', views.LoginView.as_view(), name="login")
]