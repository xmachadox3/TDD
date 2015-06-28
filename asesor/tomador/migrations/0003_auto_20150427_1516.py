# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tomador', '0002_a_investigacionoperaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='GER',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PRO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SIF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TRD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='A_InvestigacionOperaciones',
            new_name='AIO',
        ),
    ]
