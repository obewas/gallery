# Generated by Django 3.1.2 on 2020-10-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20201010_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='image',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
