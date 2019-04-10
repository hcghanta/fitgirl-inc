# Generated by Django 2.1.7 on 2019-04-10 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, unique=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('category_image', models.ImageField(blank=True, default='reward_categories/default.jpg', upload_to='reward_categories/')),
            ],
        ),
        migrations.CreateModel(
            name='RewardItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=25, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('points_needed', models.IntegerField(default=25)),
                ('qty_available', models.IntegerField(default=1)),
                ('reward_image', models.ImageField(blank=True, upload_to='reward_items/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.RewardCategory')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
