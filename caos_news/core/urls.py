from core.models import NoticiaModeracion
from core.views import buscar, clima, deportes, index, internacional, login, misnoticias, moderarnoticias, nacional, noticia, cerrar, noticiamoderacion, registrarnoticias
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('nacional', nacional, name='nacional'),
    path('internacional', internacional, name='internacional'),
    path('deportes', deportes, name='deportes'),
    path('login', login, name='login'),
    path('clima', clima, name='clima'),
    path('noticia/<id>', noticia, name='noticia'),
    path('noticiamoderacion/<id>', noticiamoderacion, name='noticiamoderacion'),
    path('buscar', buscar, name='buscar'),
    path('cerrar', cerrar, name='cerrar'),
    path('misnoticias', misnoticias, name='misnoticias'),
    path('moderarnoticias', moderarnoticias, name='moderarnoticias'),
    path('registrarnoticias', registrarnoticias, name='registrarnoticias')
]
