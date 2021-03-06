# Generated by Django 2.0.5 on 2020-09-22 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20200922_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Day')),
            ],
        ),
    ]
