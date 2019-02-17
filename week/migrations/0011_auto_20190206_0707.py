# Generated by Django 2.0.8 on 2019-02-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20190203_1041'),
        ('week', '0010_auto_20190206_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='Program',
        ),
        migrations.AddField(
            model_name='useractivity',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Program'),
        ),
    ]