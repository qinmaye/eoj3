# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0034_auto_20180703_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='pdf_statement',
            field=models.FileField(blank=True, null=True, upload_to='contest_statements/%Y%m%d/', verbose_name='PDF Statement'),
        ),
    ]
