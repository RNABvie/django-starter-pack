# Generated by Django 4.2.6 on 2023-10-25 15:34

from django.db import migrations, models
import djapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0005_worker_betteriin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='betterIIN',
        ),
        migrations.AlterField(
            model_name='worker',
            name='iin',
            field=models.CharField(max_length=13, unique=True, validators=[djapp.models.validate_numeric], verbose_name='ИИН'),
        ),
    ]
