from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'newLandList/', views.UserListView.as_view(), name="UserListView"),
    url(r'sortLand/', views.UserShortedView.as_view(id=id), name="UserShortedView"),
    url(r'approveLand/', views.UserApproved, name="ApprovedView"),
    url(r'getScatterdata/', views.getScatterdata, name="getScatterdata"),
    url(r'getHistdata/', views.getHistdata, name="getHistdata"),
]