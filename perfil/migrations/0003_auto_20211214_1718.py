# Generated by Django 3.0.2 on 2021-12-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_perfil_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='filmes_vistos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perfil',
            name='seguidores',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perfil',
            name='seguindo',
            field=models.IntegerField(default=0),
        ),
    ]
