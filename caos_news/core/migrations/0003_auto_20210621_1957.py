# Generated by Django 3.2.4 on 2021-06-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_noticia_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='url_imagen',
            field=models.CharField(default='xd', max_length=250),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NoticiaImagen',
        ),
    ]
