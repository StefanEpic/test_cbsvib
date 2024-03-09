from djoser.serializers import UserCreateSerializer, UserDeleteSerializer
from rest_framework import serializers

from users.models import Person


class PersonCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Person
        fields = ("id", "email", "password")


class PersonSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Person
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "is_active",
            "is_admin",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "is_active", "is_admin", "created_at", "updated_at")


class PersonDeleteSerializer(UserDeleteSerializer):
    pass
