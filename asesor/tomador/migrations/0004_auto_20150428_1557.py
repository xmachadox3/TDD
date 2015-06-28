# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tomador', '0003_auto_20150427_1516'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Problema',
        ),
        migrations.RemoveField(
            model_name='aio',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ger',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ntc',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pro',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sif',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trd',
            name='id',
        ),
        migrations.AlterField(
            model_name='aio',
            name='area',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='ger',
            name='area',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='area',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='pro',
            name='area',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sif',
            name='area',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='trd',
            name='area',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
