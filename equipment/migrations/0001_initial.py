# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-12-12 06:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_num', models.CharField(max_length=250, verbose_name='asset number')),
                ('desciption', models.CharField(max_length=250, verbose_name='description')),
                ('serial_num', models.CharField(max_length=250, verbose_name='serial number')),
                ('asset_type', models.CharField(max_length=250, verbose_name='asset type')),
                ('location', models.CharField(max_length=250, verbose_name='location')),
                ('status', models.CharField(choices=[('in stock', 'InStock'), ('in use', 'InUse'), ('in repair', 'InRepair'), ('broken', 'Broken')], default='in stock', max_length=10, verbose_name='asset status')),
                ('owner', models.CharField(max_length=250, verbose_name='asset owner')),
                ('assignee', models.CharField(max_length=250, verbose_name='asset assignee')),
                ('order_num', models.CharField(max_length=250, verbose_name='asset order num')),
                ('note', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_operate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
