# Generated by Django 4.2.6 on 2023-10-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0004_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='betterIIN',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=13, verbose_name='ВалидацияИИН'),
        ),
    ]
