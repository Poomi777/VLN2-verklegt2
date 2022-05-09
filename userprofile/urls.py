from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/profile
    path('', views.index, name="profile-index"),
    path('', views.userprofile, name="myprofile"),
]
