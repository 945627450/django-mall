# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classify',
            name='img',
            field=models.ImageField(blank=True, max_length=128, null=True, upload_to='classify/', verbose_name='标签主图'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='分类ID'),
        ),
    ]
