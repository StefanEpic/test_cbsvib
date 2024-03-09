from django.contrib import admin
from users.models import Person
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ("id", "email", "is_active", "is_admin")
    list_display_links = ("email",)
    list_filter = ("is_admin",)
    fieldsets = (
        ("User Credentials", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone")}),
        ("Permissions", {"fields": ("is_admin", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email", "id")
    filter_horizontal = ()


admin.site.register(Person, UserModelAdmin)
