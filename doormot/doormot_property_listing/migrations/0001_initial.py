# Generated by Django 4.2.5 on 2023-12-05 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='For_Sale_Listed_Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_by_object_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('closest_landmark', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(default=None)),
                ('property_id', models.CharField(default=None, max_length=50, unique=True)),
                ('owned_by', models.CharField(choices=[('I', 'Individual'), ('C', 'Cooperate body'), ('G', 'Government')], default=None, max_length=50)),
                ('asking_price', models.DecimalField(decimal_places=2, default=None, max_digits=12)),
                ('property_status', models.CharField(choices=[('N', 'New'), ('I', 'In use'), ('R', 'Renovated'), ('O', 'Old')], default=None, max_length=50)),
                ('property_type', models.CharField(choices=[('B', 'Bungalow'), ('D', 'Duplex'), ('DTH', 'Detached House'), ('TH', 'Terraced House'), ('BF', 'Block of Flats'), ('M', 'Mansion'), ('SC', 'Self-contained Apartment'), ('CB', 'Commercial Building'), ('RE', 'Residential Estate')], default=None, max_length=50)),
                ('sub_commercial_property_type', models.CharField(choices=[('SHP', 'Shopping Complex'), ('OS', 'Office Space'), ('SSHPU', 'Shop Units'), ('SCHL', 'School Building'), ('HSPTL', 'Hospital Building'), ('PTRLSTN', 'Petrol Station'), ('RSTRNT', 'Restaurant Building')], default=None, max_length=50)),
                ('no_of_bedrooms', models.PositiveIntegerField(default=None)),
                ('no_of_livingrooms', models.PositiveIntegerField(default=None)),
                ('no_of_bathrooms', models.PositiveIntegerField(default=None)),
                ('no_of_kitchens', models.PositiveIntegerField(default=None)),
                ('size_of_property_by_square_footage', models.PositiveIntegerField(default=None)),
                ('size_of_property_by_plot', models.PositiveIntegerField(default=None)),
                ('address', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(default=None, max_length=100)),
                ('state', models.CharField(default=None, max_length=100)),
                ('zip_code', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('local_government', models.CharField(default=None, max_length=20)),
                ('date_time_of_upload', models.DateTimeField(auto_now_add=True)),
                ('year_developed', models.DateField(default=None)),
                ('date_time_of_sale', models.DateTimeField(default=None, null=True)),
                ('is_negotiable', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('uploaded_by_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='To_Let_Listed_Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_by_object_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('closest_landmark', models.CharField(default=None, max_length=50)),
                ('description', models.TextField(default=None)),
                ('property_id', models.CharField(default=None, max_length=50, unique=True)),
                ('owned_by', models.CharField(choices=[('I', 'Individual'), ('C', 'Cooperate body'), ('G', 'Government')], default=None, max_length=50)),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_status', models.CharField(choices=[('N', 'New'), ('R', 'Renovated'), ('O', 'Old')], max_length=50)),
                ('property_type', models.CharField(choices=[('B', 'Bungalow'), ('D', 'Duplex'), ('DT', 'Detached House'), ('T', 'Terraced House'), ('BF', 'Block of Flats'), ('M', 'Mansion'), ('SC', 'Self-contained Apartment'), ('CB', 'Commercial Building'), ('RE', 'Residential Estate')], max_length=50)),
                ('sub_commercial_property_type', models.CharField(choices=[('SHP', 'Shopping Complex'), ('OS', 'Office Space'), ('SSHPU', 'Shop Units'), ('SCHL', 'School Building'), ('HSPTL', 'Hospital Building'), ('PTRLSTN', 'Petrol Station'), ('RSTRNT', 'Restaurant Building')], default=None, max_length=50)),
                ('bathroom_is_available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=50)),
                ('toilet_is_available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=50)),
                ('water_is_available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=50)),
                ('good_power_supply', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=50)),
                ('owner_lives_in_property', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=50)),
                ('address', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(default=None, max_length=100)),
                ('state', models.CharField(default=None, max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('local_government', models.CharField(default=None, max_length=20)),
                ('date_time_of_upload', models.DateTimeField(auto_now_add=True)),
                ('is_rented', models.BooleanField(default=False)),
                ('is_available_for_lease', models.BooleanField(default=False)),
                ('uploaded_by_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='To_Let_Properties_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default=None, upload_to='property_images/')),
                ('connected_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doormot_property_listing.to_let_listed_properties')),
            ],
        ),
        migrations.CreateModel(
            name='For_Sale_Properties_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default=None, upload_to='property_images/')),
                ('connected_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doormot_property_listing.for_sale_listed_properties')),
            ],
        ),
    ]
