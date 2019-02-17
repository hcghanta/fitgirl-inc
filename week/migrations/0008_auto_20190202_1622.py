# Generated by Django 2.0.8 on 2019-02-02 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0007_auto_20190202_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalpostpage',
            name='timer_for_this_activity',
            field=models.CharField(blank=True, default=datetime.time(0, 11), help_text='Time format should be in MM:SS', max_length=20),
        ),
    ]