# Generated by Django 3.2.16 on 2022-10-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='tipo',
            field=models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], default='SSD', max_length=3),
        ),
    ]
