# Generated by Django 3.0.2 on 2020-07-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bikes', '0007_auto_20200726_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddetails',
            name='Company',
            field=models.CharField(default='', max_length=500),
        ),
    ]