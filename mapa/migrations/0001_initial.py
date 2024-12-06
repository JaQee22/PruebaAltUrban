# Generated by Django 5.1.3 on 2024-11-24 00:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20, verbose_name='RUT')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('evidencia', models.ImageField(upload_to='evidencias/', verbose_name='Evidencia (JPG)')),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitud')),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('hora', models.TimeField(default=django.utils.timezone.now, verbose_name='Hora')),
                ('dias_transcurridos', models.IntegerField(default=0, verbose_name='Días transcurridos')),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')], default='Pendiente', max_length=50, verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
