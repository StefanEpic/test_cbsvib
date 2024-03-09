from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events import views

router = DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet, basename="organization")
router.register(r"events", views.EventViewSet, basename="event")

urlpatterns = [
    path("", include(router.urls)),
]
