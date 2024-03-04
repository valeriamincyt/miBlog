from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import BuscarForm
from django.utils import timezone
from .models import Post
from .busqueda import buscar
from django.shortcuts import render
import os
from django.http import FileResponse

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
    print('Ejecutando buscar_new')
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BuscarForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fuente = form["fuente"].data
            sentencia = form["sentencia"].data
            #archivoSalida = form["archivo"].data
            #buscar(fuente,sentencia,archivoSalida)
            print('Sentencia ingresada: '+ sentencia)
            buscar(fuente,sentencia)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BuscarForm()
    return render(request, "blog/buscador.html", {"form": form})

def descargar_archivo(request): 
 
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
 
    filename = 'busqueda.xlsx'
 
    filepath = BASE_DIR + '/blog/archivos/' + filename 
 
    return FileResponse(open(filepath, 'rb'), as_attachment=True)
    
