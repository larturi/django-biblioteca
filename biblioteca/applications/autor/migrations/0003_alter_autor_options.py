# Generated by Django 3.2.8 on 2021-10-12 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_rename_macionalidad_autor_nacionalidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
    ]
