from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'addlanddetail/', views.AddLandDetail, name="addlanddetail"),
    url(r'editlanddetail/', views.EditLandDetail, name="editlanddetail"),
    url(r'registration/', views.Registration, name="registration"),
    url(r'login/', views.Login, name="login"),
    url(r'showland/',views.landlist,name='landlist'),
    url(r'', views.Login, name="login"),
]