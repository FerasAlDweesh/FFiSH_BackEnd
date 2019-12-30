# Generated by Django 2.2.7 on 2019-12-30 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191224_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vendor_images'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uservendor', to=settings.AUTH_USER_MODEL),
        ),
    ]
