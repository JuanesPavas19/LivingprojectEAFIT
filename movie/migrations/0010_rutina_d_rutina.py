# Generated by Django 4.0.6 on 2022-11-07 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_dieta_d_dieta'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='d_rutina',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
