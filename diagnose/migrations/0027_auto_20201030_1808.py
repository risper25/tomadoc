# Generated by Django 3.0.6 on 2020-10-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0026_auto_20201029_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]