# Generated by Django 4.0.6 on 2022-11-15 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_imc'),
    ]

    operations = [
        migrations.CreateModel(
            name='r_rutina',
            fields=[
                ('Idr_rutina', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('Id_rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.rutina')),
                ('Id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='r_dieta',
            fields=[
                ('Idr_dieta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('Id_dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.dieta')),
                ('Id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.usuario')),
            ],
        ),
    ]
