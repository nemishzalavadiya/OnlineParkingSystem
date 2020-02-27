from django.conf.urls import url
from OnlineParkingSystem import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'registration/', views.Registration, name="Registration"),
    url(r'login/', views.Login, name="Login"),
    url(r'editprofile/', views.EditProfile, name="editprofile"),
    url(r'showlanddetails/',views.ShowLandDetails, name="showlanddetails"),
    url(r'logout/', views.LogoutHere, name="LogoutHere"),
    url(r'reserveparking/',views.ReserveParking, name="reserveparking"),
    url(r'showuserhistory/',views.ShowUserHistory,name='ShowUserHistory'),
    url(r'feedback/',views.feedback,name='feedback'),
    url(r'', views.Home, name="Home"),
]

