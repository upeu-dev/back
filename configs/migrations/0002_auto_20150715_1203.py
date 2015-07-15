# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jerarquiaacad',
            name='tipo',
            field=models.CharField(choices=[('INSTITUCION', 'INSTITUCION'), ('FACULTAD', 'FACULTAD'), ('ESCUELA', 'ESCUELA'), ('CARRERA', 'CARRERA'), ('DEPARTAMENTO', 'DEPARTAMENTO')], max_length=30),
        ),
    ]
