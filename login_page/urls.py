from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/login_page
    path('', views.index, name="login_page-index"),
]
