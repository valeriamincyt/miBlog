from django import forms
from .models import Post
import os

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        
class BuscarForm(forms.Form):
    fuente = forms.CharField(label="fuente", max_length=100)
    sentencia = forms.CharField(label="sentencia", max_length=100)
    archivo = forms.CharField(label="archivo", max_length=100)
    lista_arq = os.listdir()