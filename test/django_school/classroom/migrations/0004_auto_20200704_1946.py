# Generated by Django 2.0.1 on 2020-07-04 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200704_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup',
            name='best_by',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 4, 19, 46, 32, 583988)),
        ),
    ]
