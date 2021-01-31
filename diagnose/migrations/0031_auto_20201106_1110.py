# Generated by Django 3.0.6 on 2020-11-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0030_auto_20201106_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='pestiside',
            name='imagefile',
            field=models.ImageField(null=True, upload_to='pestisides/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='pestiside',
            name='directions',
            field=models.CharField(max_length=50000),
        ),
    ]