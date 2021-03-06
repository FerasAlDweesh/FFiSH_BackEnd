# Generated by Django 2.2.7 on 2019-12-03 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinosaur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=105)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=100)),
                ('rarity', models.CharField(choices=[('common', 'common'), ('uncommon', 'uncommon'), ('rare', 'rare'), ('exotic', 'exotic'), ('legendary', 'legendary')], max_length=105)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Dinosaur')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(through='api.OrderedItem', to='api.Dinosaur'),
        ),
    ]
