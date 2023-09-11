# Generated by Django 4.0.3 on 2023-06-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CO2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average', models.FloatField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
