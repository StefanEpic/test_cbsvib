import typing

from rest_framework import serializers

from events import models
from users.serializers import PersonSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ("id", "title", "description", "address", "postcode", "persons")
        read_only_fields = ("id",)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ("id", "title", "description", "image", "date", "organizations")
        read_only_fields = ("id",)


class OrganizationWithPersonsSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(many=True)
    address = serializers.SerializerMethodField()

    class Meta:
        model = models.Organization
        fields = ("id", "title", "description", "address", "persons")
        read_only_fields = ("id",)

    def get_address(self, obj: models.Organization) -> typing.Text:
        return f"{obj.postcode}, {obj.address}"


class EventDetailWithOrganizationSerializer(serializers.ModelSerializer):
    organizations = OrganizationWithPersonsSerializer(many=True)

    class Meta:
        model = models.Event
        fields = ("id", "title", "description", "image", "date", "organizations")
        read_only_fields = ("id",)
