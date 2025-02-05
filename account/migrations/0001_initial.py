# Generated by Django 2.1.7 on 2019-04-11 03:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Affirmations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affirmation', models.CharField(blank=True, max_length=500, null=True)),
                ('published_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CloneProgramInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_to_clone', models.CharField(max_length=25)),
                ('new_start_date', models.DateField()),
                ('new_program', models.CharField(max_length=25)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dailyquote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dailyquote', models.CharField(blank=True, max_length=500, null=True)),
                ('quote_date', models.DateField(null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inactiveuser',
            fields=[
                ('inactive_id', models.AutoField(primary_key=True, serialize=False)),
                ('set_days', models.IntegerField(default=7, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('down_at', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='InspirationalQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KindnessMessage',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(blank=True, max_length=500, null=True)),
                ('from_user', models.CharField(max_length=50)),
                ('to_user', models.CharField(max_length=50)),
                ('read_message', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_days_to_done', models.IntegerField(default=1)),
                ('nutrition_days_to_done', models.IntegerField(default=1)),
                ('rewards_active', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('current_values', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='profile_image/default.jpg', upload_to='profile_image')),
                ('bio', models.CharField(max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('secondary_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('other_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('county', models.CharField(blank=True, max_length=25, null=True)),
                ('state', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=25, null=True)),
                ('day_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('eve_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('age_group', models.IntegerField(choices=[(1, '8-10'), (2, '11-13')], null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('points', models.IntegerField(blank=True, default=0, null=True)),
                ('select_your_background_color_for_website', models.CharField(choices=[('pink', 'Pink'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange')], default='pink', max_length=50, null=True)),
                ('profile_filled', models.BooleanField(default=False)),
                ('pre_assessment', models.CharField(blank=True, default='No', max_length=50, null=True)),
                ('post_assessment', models.CharField(blank=True, default='No', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=20, unique=True)),
                ('program_start_date', models.DateField()),
                ('program_end_date', models.DateField()),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=None)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('program', models.CharField(default='Test', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('reward_no', models.AutoField(primary_key=True, serialize=False)),
                ('points_redeemed', models.IntegerField(blank=True, null=True)),
                ('service_used', models.CharField(blank=True, max_length=25, null=True)),
                ('redeem_status', models.CharField(choices=[('Yes', 'yes'), ('No', 'no')], default='No', max_length=10, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
            name='RewardsNotification',
            fields=[
                ('rewards_notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('Rewards_milestone_1', models.IntegerField(default=25)),
                ('Rewards_milestone_2', models.IntegerField(default=50)),
                ('Rewards_milestone_3', models.IntegerField(default=75)),
                ('Rewards_milestone_4', models.IntegerField(default=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('schools_id', models.AutoField(primary_key=True, serialize=False)),
                ('schools_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_days_to_done', models.IntegerField(default=1)),
                ('nutrition_days_to_done', models.IntegerField(default=1)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('current_values', models.BooleanField(default=True)),
                ('test1', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testfield2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_to_done', models.IntegerField(default=1)),
                ('nutrition_days_to_done', models.IntegerField(default=1)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('current_values', models.BooleanField(default=True)),
                ('test4', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='program',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Program'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
