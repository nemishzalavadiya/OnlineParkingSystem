from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'newLandList/', views.UserListView.as_view(), name="UserListView"),
    url(r'approveLand/', views.UserShortedView.as_view(id=id), name="UserShortedView"),
]