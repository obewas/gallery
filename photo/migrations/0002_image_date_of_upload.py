# Generated by Django 2.0 on 2020-10-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_of_upload',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
