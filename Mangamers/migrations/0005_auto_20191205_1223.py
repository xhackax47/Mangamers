# Generated by Django 3.1 on 2019-12-05 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mangamers', '0004_auto_20191205_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='videogame',
            old_name='description',
            new_name='content',
        ),
    ]
