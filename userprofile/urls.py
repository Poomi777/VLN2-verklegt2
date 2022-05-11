from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # http://localhost:8000/profile
    path('', views.index, name="profile-index"),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')

]
