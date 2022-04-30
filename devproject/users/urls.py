from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.profiles, name = 'profiles'),
    path('user-profile/<str:pk>', views.profile, name = 'user-profile'),
]