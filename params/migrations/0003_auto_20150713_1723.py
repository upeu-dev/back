# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0002_auto_20150713_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('code', models.CharField(max_length=10, blank=True, null=True)),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, to='params.Category', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('name',)]),
        ),
    ]
