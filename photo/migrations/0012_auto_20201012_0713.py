# Generated by Django 3.1.2 on 2020-10-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0011_auto_20201011_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='categories',
            field=models.ManyToManyField(choices=[], related_name='photos', to='photo.Category'),
        ),
    ]