# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190131_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'blog post', 'ordering': ['-pub_date', 'title'], 'permissions': (('view_future_post', 'Can view unpublished Post'),), 'get_latest_by': 'pub_date'},
        ),
    ]
