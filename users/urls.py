from django.urls import path, include


urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"", include("djoser.urls.jwt")),
]
