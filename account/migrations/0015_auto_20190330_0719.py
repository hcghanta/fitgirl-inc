# Generated by Django 2.0.8 on 2019-03-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20190330_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='reward_categories/'),
        ),
        migrations.AlterField(
            model_name='rewarditem',
            name='image',
            field=models.ImageField(blank=True, upload_to='reward_items/'),
        ),
    ]