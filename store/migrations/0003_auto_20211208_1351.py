# Generated by Django 3.1 on 2021-12-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_album_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_artist',
            field=models.ManyToManyField(blank=True, related_name='albums', to='store.Artist'),
        ),
    ]
