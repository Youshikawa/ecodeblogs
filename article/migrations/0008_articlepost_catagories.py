# Generated by Django 3.2.8 on 2022-07-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_rename_photo_articlepost_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='catagories',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
