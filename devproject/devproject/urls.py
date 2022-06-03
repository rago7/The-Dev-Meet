from http.client import HTTPResponse
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_view # for password reset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects', include('projects.urls')),
    path('', include('users.urls')),
    path('api/', include('api.urls')),

    # for password reset
    path('reset_password/', auth_view.PasswordResetView.as_view(), name='reset_password')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
