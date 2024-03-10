# Generated by Django 4.2 on 2024-03-10 10:22

from django.conf import settings
from django.db import migrations, models
import events.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("address", models.CharField(max_length=255)),
                ("postcode", models.CharField(max_length=6, validators=[events.validators.validate_postcode_field])),
                ("persons", models.ManyToManyField(related_name="organizations", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("image", models.URLField()),
                ("date", models.DateField()),
                ("organizations", models.ManyToManyField(related_name="events", to="events.organization")),
            ],
        ),
    ]
