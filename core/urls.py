"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views

from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", include("chat.urls")),
    path(
        "api/v1/",
        include(
            [
                path("", include("users.urls")),
                path("", include("events.urls")),
                path("schema/", views.SpectacularAPIView.as_view(), name="schema"),
                path("schema/swagger-ui/", views.SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
                path("schema/redoc/", views.SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
            ]
        ),
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
