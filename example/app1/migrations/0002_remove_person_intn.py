# Generated by Django 2.2.5 on 2019-09-15 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='intn',
        ),
    ]
