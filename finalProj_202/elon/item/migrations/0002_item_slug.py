# Generated by Django 3.1.7 on 2021-04-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
    ]
