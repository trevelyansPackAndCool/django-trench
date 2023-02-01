# Generated by Django 4.1.5 on 2023-02-01 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trench", "0004_alter_mfamethod_id_mfamethod_unique_user_is_primary_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="mfamethod",
            name="primary_is_active",
        ),
        migrations.AddField(
            model_name="mfamethod",
            name="counter",
            field=models.PositiveIntegerField(default=0, verbose_name="counter"),
        ),
        migrations.AddField(
            model_name="mfamethod",
            name="is_totp",
            field=models.BooleanField(default=True, verbose_name="is totp"),
        ),
        migrations.AlterField(
            model_name="mfamethod",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AddConstraint(
            model_name="mfamethod",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(("is_primary", True), ("is_active", True)),
                    ("is_primary", False),
                    _connector="OR",
                ),
                name="primary_is_active",
            ),
        ),
    ]