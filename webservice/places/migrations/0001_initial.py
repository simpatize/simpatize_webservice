# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('place_type', models.CharField(max_length=100)),
                ('geolocation', models.CharField(max_length=100)),
                ('cause', models.CharField(max_length=20)),
            ],
        ),
    ]
