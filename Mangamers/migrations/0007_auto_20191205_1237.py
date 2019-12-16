# Generated by Django 3.1 on 2019-12-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mangamers', '0006_videogame_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='manga',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='videogame',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='release_date',
            field=models.DateTimeField(verbose_name='Date de sortie'),
        ),
    ]