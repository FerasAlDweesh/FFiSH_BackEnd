# Generated by Django 2.2.7 on 2019-12-19 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191219_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='customer',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='staff',
            new_name='user',
        ),
    ]