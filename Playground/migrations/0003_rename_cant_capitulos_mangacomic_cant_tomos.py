# Generated by Django 4.0.4 on 2022-06-07 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Playground', '0002_alter_animeserie_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mangacomic',
            old_name='cant_capitulos',
            new_name='cant_tomos',
        ),
    ]
