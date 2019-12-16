# Generated by Django 3.1 on 2019-12-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('type_manga', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('release_date', models.DateTimeField(verbose_name='Date de parution')),
            ],
        ),
    ]