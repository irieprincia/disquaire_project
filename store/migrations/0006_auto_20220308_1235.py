# Generated by Django 3.2.12 on 2022-03-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_album_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'disque'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'artiste'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'réservation'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'client'},
        ),
        migrations.AddField(
            model_name='album',
            name='commande',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='album',
            name='storage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(upload_to='disquaire_project'),
        ),
    ]