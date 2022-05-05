from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),


    path('', views.profiles, name = 'profiles'),
    path('user-profile/<str:pk>', views.profile, name = 'user-profile'),
    path('account', views.userAccount, name='account')
]