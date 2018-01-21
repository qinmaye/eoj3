# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-28 13:27
from __future__ import unicode_literals

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20170914_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, unique=True, validators=[account.models.UsernameValidator()], verbose_name='username'),
        ),
    ]