# Generated by Django 4.0.2 on 2022-06-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactoform_alter_producto_id_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
    ]
