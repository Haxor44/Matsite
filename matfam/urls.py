from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.url import staticfiles_urlpatterns
urlpatterns = [
    path("matfamApp/", include("matfamApp.urls")),
    path("admin/", admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
