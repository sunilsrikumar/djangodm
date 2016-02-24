# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
        ('products', '0015_product_sale_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='managers',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=2, to='sellers.SellerAccount'),
            preserve_default=False,
        ),
    ]
