# Generated by Django 2.1.7 on 2019-04-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20190331_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
