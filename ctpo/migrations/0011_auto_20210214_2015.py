# Generated by Django 3.1.5 on 2021-02-14 20:15

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ctpo', '0010_merge_20210214_2015'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('bject', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='on_top',
        ),
    ]