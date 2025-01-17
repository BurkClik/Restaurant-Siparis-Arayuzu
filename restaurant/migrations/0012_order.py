# Generated by Django 3.0.6 on 2020-05-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_auto_20200519_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderer_name', models.CharField(max_length=100)),
                ('orderer_surname', models.CharField(max_length=100)),
                ('orderer_email', models.EmailField(max_length=254)),
                ('orderer_phone', models.CharField(max_length=11)),
                ('orderer_address', models.CharField(max_length=200)),
                ('order_price', models.FloatField()),
                ('order_detail', models.TextField()),
            ],
        ),
    ]
