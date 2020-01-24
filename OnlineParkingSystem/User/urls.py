from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'registration/', views.Registration, name="registration"),
    url(r'login/', views.Login, name="login"),
    url(r'editprofile/', views.EditProfile, name="editprofile"),
    url(r'showlanddetails/',views.ShowLandDetails.as_view(), name="showlanddetails"),
    url(r'', views.Login, name="login"),
]
