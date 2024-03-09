from typing import Text

from django.db import models

from events.validators import validate_postcode_field
from users.models import Person


class Organization(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=6, validators=[validate_postcode_field])
    persons = models.ManyToManyField(Person, related_name="organizations")

    def __str__(self) -> Text:
        return str(self.title)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.URLField()
    date = models.DateField()
    organizations = models.ManyToManyField(Organization, related_name="events")

    def __str__(self) -> Text:
        return str(self.title)
