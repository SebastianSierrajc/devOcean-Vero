# Generated by Django 3.2.7 on 2021-10-26 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentimientoInicial', models.CharField(max_length=255)),
                ('sentimientoFinal', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]