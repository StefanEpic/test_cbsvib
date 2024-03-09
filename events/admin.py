import typing

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from events import models


class PersonsInline(admin.TabularInline):
    model = models.Organization.persons.through
    extra = 1
    verbose_name = "Person"


class OrganizationInline(admin.TabularInline):
    model = models.Event.organizations.through
    extra = 1
    verbose_name = "Organization"


class OrganizationModelAdmin(ModelAdmin):
    list_display = ("id", "title", "address", "postcode")
    list_display_links = ("title",)
    list_filter = ("postcode",)
    fieldsets = (("Organization info", {"fields": ("title", "description", "address", "postcode")}),)
    inlines = (PersonsInline,)
    search_fields = ("title", "address", "postcode")
    ordering = ("title", "id")
    filter_horizontal = ()


class EventModelAdmin(ModelAdmin):
    list_display = ("id", "title", "date", "get_image")
    list_display_links = ("title",)
    list_filter = ("date",)
    fieldsets = (("Event info", {"fields": ("title", "description", "image", "date")}),)
    inlines = (OrganizationInline,)
    search_fields = ("title", "date")
    ordering = ("title", "id")
    filter_horizontal = ()

    def get_image(self, obj: models.Event) -> typing.Text:
        return mark_safe(f'<img src={obj.image} width="100" height="100"')


admin.site.register(models.Organization, OrganizationModelAdmin)
admin.site.register(models.Event, EventModelAdmin)
