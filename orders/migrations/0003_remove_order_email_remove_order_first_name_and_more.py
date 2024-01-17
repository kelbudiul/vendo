# Generated by Django 5.0.1 on 2024-01-17 11:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_orderitem_vendor"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="email",
        ),
        migrations.RemoveField(
            model_name="order",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="last_name",
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]