# Generated by Django 4.0.4 on 2022-06-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Playground', '0003_rename_cant_capitulos_mangacomic_cant_tomos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangacomic',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
