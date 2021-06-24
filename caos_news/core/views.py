from core.models import CategoriaNoticia, Noticia
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login as login_aut


def index(request):
    noticias = Noticia.objects.filter(publicar=True).order_by('-id')[:10]
    portada = Noticia.objects.filter(
        publicar=True, portada=True).order_by('-timestamp')[:6]
    contexto = {"noticias": noticias, "portada": portada}
    return render(request, "index.html", contexto)


def nacional(request):
    noticias = Noticia.objects.filter(
        publicar=True, CategoriaNoticia_id=1).order_by('-id')[:10]
    portada = Noticia.objects.filter(
        publicar=True, portada=True, CategoriaNoticia_id=1).order_by('-timestamp')[:3]
    contexto = {"noticias": noticias, "portada": portada}
    return render(request, 'nacional.html', contexto)


def internacional(request):
    noticias = Noticia.objects.filter(
        publicar=True, CategoriaNoticia_id=2).order_by('-id')[:10]
    portada = Noticia.objects.filter(
        publicar=True, portada=True, CategoriaNoticia_id=2).order_by('-timestamp')[:3]
    contexto = {"noticias": noticias, "portada": portada}
    return render(request, 'internacional.html', contexto)


def deportes(request):
    noticias = Noticia.objects.filter(
        publicar=True, CategoriaNoticia_id=3).order_by('-id')[:10]
    portada = Noticia.objects.filter(
        publicar=True, portada=True, CategoriaNoticia_id=3).order_by('-timestamp')[:3]
    contexto = {"noticias": noticias, "portada": portada}
    return render(request, 'internacional.html', contexto)


def login(request):
    if request.user.is_authenticated:
        response = redirect('index')
        return response

    mensaje = ""
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request, us)
            noticias = Noticia.objects.filter(
                publicar=True).order_by('-id')[:10]
            portada = Noticia.objects.filter(
                publicar=True, portada=True).order_by('-timestamp')[:6]
            contexto = {"noticias": noticias, "portada": portada}
            response = redirect('index')
            return response
        else:
            mensaje = "Error"
    contexto = {'mensaje': mensaje}
    return render(request, 'login.html', contexto)


def clima(request):
    return render(request, "clima.html")


def noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    if noticia.publicar:
        contexto = {"noticia": noticia}
        return render(request, "noticia.html", contexto)
    else:
        response = redirect('index')
        return response


def noticiamoderacion(request, id):
    noticia = Noticia.objects.get(id=id)
    if not noticia.publicar:
        contexto = {"noticia": noticia}
        return render(request, "noticia.html", contexto)
    else:
        response = redirect('index')
        return response


def cerrar(request):
    logout(request)
    noticias = Noticia.objects.filter(publicar=True).order_by('-id')[:10]
    portada = Noticia.objects.filter(
        publicar=True, portada=True).order_by('-timestamp')[:6]
    contexto = {"noticias": noticias, "portada": portada}
    return render(request, "index.html", contexto)


def buscar(request):
    if request.POST:
        buscarTitular = request.POST.get("txtBuscar")
        noticias = Noticia.objects.filter(
            titular__contains=buscarTitular, publicar=True, portada=True).order_by('-timestamp')
        contexto = {"noticias": noticias, "buscarTitular": buscarTitular}
        return render(request, "buscar.html", contexto)
    else:
        noticias = Noticia.objects.filter(publicar=True).order_by('-id')[:10]
        portada = Noticia.objects.filter(
            publicar=True, portada=True).order_by('-timestamp')[:6]
        contexto = {"noticias": noticias, "portada": portada}
        return render(request, "index.html", contexto)


def misnoticias(request):
    usuario = request.user.username
    if not request.user.is_staff:
        noticias = Noticia.objects.filter(
            publicar=False, user=usuario).order_by('-id')
        categorias = CategoriaNoticia.objects.all()
        contexto = {'noticias': noticias, 'categorias': categorias}
        return render(request, "misnoticias.html", contexto)
    else:
        response = redirect('index')
        return response


def moderarnoticias(request):
    usuario = request.user.username
    return render(request, "moderarnoticias.html")


def registrarnoticias(request):
    usuario = request.user.username

    if not request.user.is_staff:
        if request.POST:
            noticia = Noticia()
            categoria = CategoriaNoticia.objects.get(
                id=request.POST.get('cmbCategoria'))
            noticia.CategoriaNoticia = categoria
            noticia.user = usuario
            noticia.titular = request.POST.get('txtTitulo')
            noticia.epigrafe = request.POST.get('txtEpigrafe')
            noticia.url_imagen = request.POST.get('txtImagen')
            noticia.contenido = request.POST.get('txtNoticia')
            noticia.save()
            response = redirect('misnoticias')
            return response
    else:
        response = redirect('misnoticias')
        return response
