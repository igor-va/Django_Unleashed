# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0007_auto_20190131_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(to='organizer.Startup'),
        ),
    ]
