# Generated by Django 3.1 on 2020-08-23 20:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersAccount', '0002_userprofileinfo_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
