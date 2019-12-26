from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'registration/', views.RegistrationView.as_view(), name="registration"),
    url(r'login/', views.LoginView.as_view(), name="login"),
    url(r'', views.LoginView.as_view(), name="login"),
    url(r'loginClass/', views.LoginViewClass.as_view(),name='LoginViewClass'),
]