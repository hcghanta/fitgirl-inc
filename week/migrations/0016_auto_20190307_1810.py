# Generated by Django 2.0.8 on 2019-03-08 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0015_merge_20190307_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtemplates',
            name='rewards_message',
        ),
        migrations.RemoveField(
            model_name='emailtemplates',
            name='subject_for_rewards_notification',
        ),
    ]
