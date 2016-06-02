# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=1500)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=1500)),
                ('fechainicio', models.DateTimeField(null=True)),
                ('fechafin', models.DateTimeField(null=True)),
                ('fecharegistro', models.DateTimeField(auto_now=True)),
                ('fechalimite', models.DateTimeField(null=True)),
                ('estatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='porhacer.Estatus')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='porhacer.Proyecto')),
            ],
        ),
    ]
