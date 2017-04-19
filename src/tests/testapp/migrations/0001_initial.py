# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django_l10n_extensions.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='I18NTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i18n_field', django_l10n_extensions.models.fields.I18NField(max_length=128)),
            ],
        ),
    ]