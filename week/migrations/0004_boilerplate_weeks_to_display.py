# Generated by Django 2.0.8 on 2019-01-30 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0003_auto_20190129_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='boilerplate',
            name='weeks_to_display',
            field=models.ManyToManyField(related_name='_boilerplate_weeks_to_display_+', to='week.BoilerPlate'),
        ),
    ]