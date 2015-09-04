# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('image', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
            ],
        ),
    ]
