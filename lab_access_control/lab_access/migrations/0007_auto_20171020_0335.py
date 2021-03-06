# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab_access', '0006_auto_20171020_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='bancada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_access.Bancada'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='hora_fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='hora_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_access.Laboratorio'),
        ),
    ]
