# Generated by Django 3.1 on 2019-12-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mangamers', '0009_auto_20191205_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='img',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Y0771889\\PycharmProjects\\ProjectMangamers\\media/'),
        ),
        migrations.AddField(
            model_name='manga',
            name='img',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Y0771889\\PycharmProjects\\ProjectMangamers\\media/'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='img',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Y0771889\\PycharmProjects\\ProjectMangamers\\media/'),
        ),
    ]