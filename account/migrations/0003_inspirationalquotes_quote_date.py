# Generated by Django 2.0.8 on 2019-01-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190126_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspirationalquotes',
            name='quote_date',
            field=models.DateField(null=True),
        ),
    ]