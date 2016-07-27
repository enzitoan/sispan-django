# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_remove_detalle_cantidad_panes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='fecha_entrega',
            field=models.DateField(default=datetime.datetime(2016, 7, 27, 13, 25, 53, 395319, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='fecha_pedido',
            field=models.DateField(default=datetime.datetime(2016, 7, 27, 13, 25, 53, 395268, tzinfo=utc)),
        ),
    ]
