# Generated by Django 3.2 on 2021-05-06 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='add_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество'),
        ),
    ]
