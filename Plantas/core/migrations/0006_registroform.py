# Generated by Django 4.0.4 on 2022-07-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroForm',
            fields=[
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('correo', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Correo')),
                ('contrasena', models.CharField(max_length=20, verbose_name='Contrasena')),
            ],
        ),
    ]