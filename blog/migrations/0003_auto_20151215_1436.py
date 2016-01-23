# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_emailsubscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscribers',
            name='email',
            field=models.TextField(unique=True, max_length=200),
        ),
    ]
