# Generated by Django 4.0 on 2021-12-28 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
