# Generated by Django 2.0.5 on 2020-09-22 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date'),
        ),
    ]