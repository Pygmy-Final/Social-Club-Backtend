# Generated by Django 4.0 on 2021-12-28 19:24

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_event_eventcreator'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='EventParticipants',
            field=django_mysql.models.ListTextField(models.IntegerField(), null=True, size=50),
        ),
    ]