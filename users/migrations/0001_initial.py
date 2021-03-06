# Generated by Django 4.0 on 2021-12-28 17:08

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('profilePicture', models.ImageField(upload_to='')),
                ('interests', multiselectfield.db.fields.MultiSelectField(choices=[('Reading', 'Reading'), ('Cycling', 'Cycling'), ('Hiking', 'Hiking'), ('Drawing', 'Drawing'), ('Photography', 'Photography'), ('Swimming', 'Swimming'), ('Sleeping', 'Sleeping'), ('Sports', 'Sports'), ('Gaming', 'Gaming')], max_length=256)),
            ],
        ),
    ]
