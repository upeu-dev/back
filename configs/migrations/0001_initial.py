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
                ('abrev', models.CharField(blank=True, null=True, max_length=10)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Carreras',
                'verbose_name': 'Carrera',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(blank=True, null=True, max_length=10)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Escuelas',
                'verbose_name': 'Escuela',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(blank=True, null=True, max_length=10)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Facultades',
                'verbose_name': 'Facultad',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(blank=True, null=True, max_length=10)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
                ('estructura_validada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
                'verbose_name': 'Institución',
            },
        ),
        migrations.CreateModel(
            name='JerarquiaAcad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tipo', models.CharField(choices=[('INSTITUCION', 'INSTITUCION'), ('FACULTAD', 'FACULTAD'), ('ESCUELA', 'ESCUELA'), ('CARRERA', 'CARRERA'), ('DEPARTAMENTO', 'DEPARTAMENTO')], max_length=10)),
                ('institucion', models.ForeignKey(blank=True, null=True, to='configs.Institucion')),
                ('parent', models.ForeignKey(blank=True, null=True, to='configs.JerarquiaAcad')),
            ],
            options={
                'verbose_name_plural': 'JerarquiaAcads',
                'verbose_name': 'JerarquiaAcad',
            },
        ),
        migrations.AddField(
            model_name='institucion',
            name='jerarquia_acad',
            field=models.ForeignKey(blank=True, null=True, related_name='institucion_set', to='configs.JerarquiaAcad'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='jerarquia_acad',
            field=models.ForeignKey(blank=True, null=True, to='configs.JerarquiaAcad'),
        ),
        migrations.AddField(
            model_name='escuela',
            name='jerarquia_acad',
            field=models.ForeignKey(blank=True, null=True, to='configs.JerarquiaAcad'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='jerarquia_acad',
            field=models.ForeignKey(blank=True, null=True, to='configs.JerarquiaAcad'),
        ),
    ]
