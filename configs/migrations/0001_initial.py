# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, null=True, blank=True)),
                ('codigo', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, null=True, blank=True)),
                ('codigo', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Escuela',
                'verbose_name_plural': 'Escuelas',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, null=True, blank=True)),
                ('codigo', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, null=True, blank=True)),
                ('codigo', models.CharField(max_length=10, null=True, blank=True)),
                ('estructura_validada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Institución',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='JerarquiaAcad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tipo', models.CharField(max_length=30, choices=[('INSTITUCION', 'INSTITUCION'), ('FACULTAD', 'FACULTAD'), ('ESCUELA', 'ESCUELA'), ('CARRERA', 'CARRERA'), ('DEPARTAMENTO', 'DEPARTAMENTO')])),
                ('institucion', models.ForeignKey(to='configs.Institucion', null=True, blank=True)),
                ('parent', models.ForeignKey(to='configs.JerarquiaAcad', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'JerarquiaAcad',
                'verbose_name_plural': 'JerarquiaAcads',
            },
        ),
        migrations.AddField(
            model_name='institucion',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', related_name='institucion_set', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='facultad',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='escuela',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', null=True, blank=True),
        ),
    ]
