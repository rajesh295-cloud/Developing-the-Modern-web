# Generated by Django 3.0.2 on 2020-07-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bikes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='Bike_name',
            new_name='Bikename',
        ),
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='desc',
            new_name='Desc',
        ),
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='Engine_Displacement',
            new_name='EngineDisplacement',
        ),
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='fuel',
            new_name='Fuel',
        ),
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='gear',
            new_name='Gear',
        ),
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='max_torque',
            new_name='maxpower',
        ),
        migrations.RenameField(
            model_name='uploaddetails',
            old_name='max_power',
            new_name='maxtorque',
        ),
    ]
