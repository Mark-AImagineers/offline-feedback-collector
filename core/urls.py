from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from core.views import landing_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landing_view, name="landing"),
    path("", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
