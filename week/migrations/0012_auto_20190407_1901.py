# Generated by Django 2.1.7 on 2019-04-08 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0011_postassessmentpage_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postassessmentpage',
            old_name='post_image',
            new_name='display_image',
        ),
    ]
