# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-03 04:47
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('mysite', '0008_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='product',
            name='website',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=filer.fields.image.FilerImageField(default=b'', on_delete=django.db.models.deletion.CASCADE, related_name='category_image', to='filer.Image'),
        ),
    ]