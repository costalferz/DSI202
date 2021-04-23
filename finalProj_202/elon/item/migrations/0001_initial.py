# Generated by Django 3.1.7 on 2021-04-17 17:12

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('slug', models.SlugField(default=None, unique=True)),
            ],
            options={
                'verbose_name_plural': 'หมวดหมู่',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemid', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=300)),
                ('detail', models.TextField(max_length=1000)),
                ('img', models.ImageField(default='default_item.png', upload_to='item_pics')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='item.category')),
            ],
            options={
                'verbose_name_plural': 'สินค้า',
            },
        ),
        migrations.CreateModel(
            name='itemHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('trackNum', models.CharField(max_length=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ประวัติการสั่งซื้อ',
            },
        ),
    ]