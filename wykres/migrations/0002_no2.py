# Generated by Django 4.0.3 on 2023-06-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wykres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NO2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average', models.FloatField()),
            ],
        ),
    ]
