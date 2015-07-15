# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jerarquiaacad',
            options={'verbose_name': 'JerarquiaAcad', 'verbose_name_plural': 'JerarquiaAcads'},
        ),
        migrations.AlterField(
            model_name='institucion',
            name='jerarquia_acad',
            field=models.ForeignKey(related_name='institucion_set', null=True, blank=True, to='configs.JerarquiaAcad'),
        ),
    ]
