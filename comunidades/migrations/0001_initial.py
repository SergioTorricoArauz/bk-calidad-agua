# Generated by Django 5.1.3 on 2024-12-05 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provincias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComunidadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunidades', to='provincias.provinciamodel')),
            ],
        ),
    ]
