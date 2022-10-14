# Generated by Django 4.1.1 on 2022-10-09 08:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_savedcourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcourses',
            name='activate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 9, 1, 4, 10, 79460)),
        ),
        migrations.AlterField(
            model_name='savedcourses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
    ]