# Generated by Django 3.0.2 on 2020-07-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bikes', '0003_auto_20200726_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaddetails',
            name='file',
        ),
        migrations.AddField(
            model_name='uploaddetails',
            name='image',
            field=models.ImageField(default='null', upload_to='pictures'),
        ),
    ]