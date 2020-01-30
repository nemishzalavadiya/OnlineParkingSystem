from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'registration/', views.Registration, name="registration"),
    url(r'login/', views.Login, name="login"),
    url(r'editprofile/', views.EditProfile, name="editprofile"),
    url(r'showlanddetails/',views.ShowLandDetails, name="showlanddetails"),
    url(r'reserveparking/',views.ReserveParking, name="reserveparking"),
    url(r'', views.Login, name="login"),
]
