# Generated by Django 3.2.16 on 2022-10-14 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('procesador', models.CharField(max_length=100)),
                ('memoria', models.CharField(max_length=100)),
                ('disco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asig', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_entr', models.DateTimeField()),
                ('key_Equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.equipo')),
                ('key_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
