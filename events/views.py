import typing

import requests
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from events import docs, models
from events import serializers


@docs.organization_summary
class OrganizationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticated]


@docs.event_summary
class EventViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Event.objects.all().order_by("-date")
    serializer_class = serializers.EventSerializer
    search_fields = ("date", "title")
    ordering_fields = ("date",)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    permission_classes = [IsAuthenticated]

    def retrieve(self, request: requests.Request, *args: typing.Any, **kwargs: typing.Any) -> Response:
        instance = self.get_object()
        serializer = serializers.EventDetailWithOrganizationSerializer(instance)
        return Response(serializer.data)
