# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=8, max_digits=17)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='exchange.Currency')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Currency')),
            ],
        ),
    ]
