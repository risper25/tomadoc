# Generated by Django 3.0.6 on 2020-12-15 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0042_auto_20201215_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='result',
        ),
    ]
