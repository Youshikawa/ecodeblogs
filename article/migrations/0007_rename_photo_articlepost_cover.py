# Generated by Django 3.2.8 on 2022-07-08 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_articlepost_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='photo',
            new_name='cover',
        ),
    ]
