# Generated by Django 4.0.3 on 2023-09-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wykres', '0005_pm10_pm25'),
    ]

    operations = [
        migrations.AlterField(
            model_name='no2',
            name='date',
            field=models.DateTimeField(),
        ),
    ]