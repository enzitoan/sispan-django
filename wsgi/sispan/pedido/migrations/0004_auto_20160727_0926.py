# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_auto_20160727_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='fecha_entrega',
            field=models.DateField(default=b''),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='fecha_pedido',
            field=models.DateField(default=b''),
        ),
    ]
