from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import BuscarForm
from django.utils import timezone
from .models import Post
from .busqueda import buscar
#from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def post_list(request):
    posts = ['Hola','como','estas?']
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def buscar_new(request):
    #buscar()
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BuscarForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fuente = form["fuente"].data
            sentencia = form["sentencia"].data
            archivoSalida = form["archivo"].data
            buscar(fuente,sentencia,archivoSalida)
            #return HttpResponseRedirect("")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BuscarForm()
    return render(request, "blog/buscador.html", {"form": form})

#def buscador(request):
#    sentencia = 'Inteligencia Artificial'
#    return render(request, 'blog/post_list.html', {'sentencia': sentencia}) 