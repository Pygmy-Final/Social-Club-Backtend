# Generated by Django 4.0 on 2021-12-28 17:39

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_people_gender_alter_people_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=26),
        ),
        migrations.AlterField(
            model_name='people',
            name='firstname',
            field=models.CharField(max_length=26),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=26),
        ),
        migrations.AlterField(
            model_name='people',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Reading', 'Reading'), ('Cycling', 'Cycling'), ('Hiking', 'Hiking'), ('Drawing', 'Drawing'), ('Photography', 'Photography'), ('Swimming', 'Swimming'), ('Sleeping', 'Sleeping'), ('Sports', 'Sports'), ('Gaming', 'Gaming')], max_length=26),
        ),
        migrations.AlterField(
            model_name='people',
            name='lastname',
            field=models.CharField(max_length=26),
        ),
    ]
