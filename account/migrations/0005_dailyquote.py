# Generated by Django 2.0.8 on 2019-01-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_inspirationalquotes_quote_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dailyquote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dailyquote', models.CharField(blank=True, max_length=500, null=True)),
                ('quote_date', models.DateField(null=True)),
            ],
        ),
    ]