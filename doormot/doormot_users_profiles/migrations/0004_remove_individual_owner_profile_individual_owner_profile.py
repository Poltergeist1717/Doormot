# Generated by Django 4.2.5 on 2023-11-15 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doormot_users_profiles', '0003_rename_private_owner_user_individual_owner_profile_individual_owner_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual_owner_profile',
            name='Individual_owner_profile',
        ),
    ]
