from django.db import models
from django.db.models.deletion import CASCADE


class CategoriaNoticia(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} {self.nombre}'


class Noticia(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    CategoriaNoticia = models.ForeignKey(
        CategoriaNoticia, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_created=True,auto_now_add=True)
    user = models.CharField(max_length=50)
    titular = models.TextField()
    epigrafe = models.TextField()
    url_imagen = models.CharField(max_length=250)
    contenido = models.TextField()
    publicar = models.BooleanField(default=False)
    portada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.CategoriaNoticia.nombre} {self.titular}'


class NoticiaModeracion(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    Noticia = models.ForeignKey(Noticia, on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_created=True)
    user = models.CharField(max_length=50)
    comentario = models.TextField()
