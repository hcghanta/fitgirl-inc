# Generated by Django 2.0.8 on 2019-03-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20190330_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardcategory',
            name='image',
            field=models.ImageField(blank=True, default='reward_categories/default.jpg', upload_to='reward_categories/'),
        ),
    ]
