from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('candidate/add/', register_candidate, name='register_candidate'),
    path('voter/add/', register_voter, name='register_voter'),
    path('login/', login_user, name='login'),
    path('logout/',logout_user,name='logout'),
]