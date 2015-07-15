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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, blank=True, null=True)),
                ('codigo', models.CharField(max_length=10, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Carreras',
                'verbose_name': 'Carrera',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, blank=True, null=True)),
                ('codigo', models.CharField(max_length=10, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Escuelas',
                'verbose_name': 'Escuela',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, blank=True, null=True)),
                ('codigo', models.CharField(max_length=10, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Facultades',
                'verbose_name': 'Facultad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10, blank=True, null=True)),
                ('codigo', models.CharField(max_length=10, blank=True, null=True)),
                ('estructura_validada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
                'verbose_name': 'Institución',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JerarquiaAcad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('institucion', models.ForeignKey(to='configs.Institucion', blank=True, null=True)),
                ('parent', models.ForeignKey(to='configs.JerarquiaAcad', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
                'verbose_name': 'Institución',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='institucion',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', related_name='institucion_e', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facultad',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='escuela',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carrera',
            name='jerarquia_acad',
            field=models.ForeignKey(to='configs.JerarquiaAcad', blank=True, null=True),
            preserve_default=True,
        ),
    ]
