# Generated by Django 4.2.5 on 2023-12-30 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doormot_reg_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doormot_user_independent_agent',
            name='locked_account_count_down_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]