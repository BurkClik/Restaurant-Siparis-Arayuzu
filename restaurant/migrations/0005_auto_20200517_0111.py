# Generated by Django 3.0.6 on 2020-05-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200517_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='food_image',
            field=models.ImageField(default='../static/images/kebab.jpg', upload_to='static/images/'),
        ),
    ]
