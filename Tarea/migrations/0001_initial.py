# Generated by Django 5.1.1 on 2024-09-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='I', max_length=100)),
            ],
        ),
    ]
