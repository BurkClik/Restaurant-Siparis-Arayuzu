# Generated by Django 3.0.6 on 2020-05-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200517_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='food_image',
            field=models.ImageField(default='../static/images/kebab.jpg', upload_to='foods'),
        ),
    ]
