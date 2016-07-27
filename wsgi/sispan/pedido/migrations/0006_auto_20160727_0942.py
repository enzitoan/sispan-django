# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_auto_20160727_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='fecha_entrega',
            field=models.DateField(default=datetime.datetime(2016, 7, 27, 13, 42, 12, 170379, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='fecha_pedido',
            field=models.DateField(default=datetime.datetime(2016, 7, 27, 13, 42, 12, 170328, tzinfo=utc)),
        ),
    ]
