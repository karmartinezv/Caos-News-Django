# Generated by Django 3.2.3 on 2021-06-23 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210621_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaModeracion',
            fields=[
                ('timestamp', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('comentario', models.TextField()),
                ('Noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.noticia')),
            ],
        ),
    ]
