# Generated by Django 4.2.8 on 2023-12-18 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_purchaseorder_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
