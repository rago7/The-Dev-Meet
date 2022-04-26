from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.profiles, name = 'profiles'),
    path('user-profile/<str:pk>', views.profile, name = 'user-profile'),
]