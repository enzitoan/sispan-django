# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fecha_pedido', models.DateField(default=datetime.date.today)),
                ('fecha_entrega', models.DateField()),
                ('cantidad_pita_integral', models.IntegerField(default=0)),
                ('cantidad_pita_blanco', models.IntegerField(default=0)),
                ('cantidad_amasado_integral', models.IntegerField(default=0)),
                ('cantidad_amasado_blanco', models.IntegerField(default=0)),
                ('cantidad_panes', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=70)),
                ('descripcion', models.TextField(max_length=100)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]
