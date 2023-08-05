from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("matfamApp/", include("matfamApp.urls")),
    path("admin/", admin.site.urls),
]