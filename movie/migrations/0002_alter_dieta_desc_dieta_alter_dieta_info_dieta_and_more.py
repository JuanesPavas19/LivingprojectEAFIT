# Generated by Django 4.0.6 on 2022-10-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieta',
            name='desc_dieta',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='info_dieta',
            field=models.CharField(max_length=2550),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='desc_rutina',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='info_rutina',
            field=models.CharField(max_length=2550),
        ),
    ]