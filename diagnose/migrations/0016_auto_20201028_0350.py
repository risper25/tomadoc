# Generated by Django 3.0.6 on 2020-10-28 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0015_auto_20201028_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='diagnose.ImageModel'),
        ),
    ]
