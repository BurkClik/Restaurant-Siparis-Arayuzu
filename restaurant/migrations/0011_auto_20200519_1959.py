# Generated by Django 3.0.6 on 2020-05-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20200518_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='food_desc',
            field=models.CharField(default='Yemek', max_length=150),
        ),
        migrations.AlterField(
            model_name='menu',
            name='food_name',
            field=models.CharField(max_length=50),
        ),
    ]
