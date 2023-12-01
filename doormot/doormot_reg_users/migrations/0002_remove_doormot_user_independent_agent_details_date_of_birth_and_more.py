# Generated by Django 4.2.5 on 2023-11-28 20:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doormot_reg_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doormot_user_independent_agent_details',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='doormot_user_official_agent_details',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='doormot_user_independent_agent',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='doormot_user_official_agent',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='doormot_user_independent_agent',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_individual_buyer',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_individual_owner',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_individual_tenant',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_official_agent',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_private_organization_buyer',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_private_organization_owner',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doormot_user_private_organization_tenant',
            name='false_log_count',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
