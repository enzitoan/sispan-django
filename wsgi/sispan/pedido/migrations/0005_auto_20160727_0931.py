# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20160727_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='fecha_entrega',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='fecha_pedido',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
