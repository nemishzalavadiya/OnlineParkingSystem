from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'addlanddetail/', views.AddLandDetail, name="addlanddetail"),
    url(r'editlanddetail/', views.EditLandDetail, name="editlanddetail"),
    url(r'showland/',views.landlist,name='landlist'),
    url(r'showhistory/',views.ShowHistory,name='ShowHistory'),
    url(r'deleteland/',views.DeleteLand,name='deleteland'),
    url(r'payment/',views.Payment,name='payment'),
]