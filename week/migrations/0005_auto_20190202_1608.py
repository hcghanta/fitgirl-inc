# Generated by Django 2.0.8 on 2019-02-02 22:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('week', '0004_boilerplate_weeks_to_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=50)),
                ('Week', models.IntegerField()),
                ('Points Available', models.IntegerField()),
                ('Points Earned', models.IntegerField()),
                ('creation_date', models.DateField(default=datetime.date(2019, 2, 2))),
                ('updated_date', models.DateField(default=datetime.date(2019, 2, 2))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),

    ]