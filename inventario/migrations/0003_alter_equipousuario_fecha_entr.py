# Generated by Django 3.2.16 on 2022-10-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_equipo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipousuario',
            name='fecha_entr',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
