from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_new, name='buscar_new'),
    #path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('buscar/', views.buscar_new, name='buscar_new'),
    path('descargar/', views.descargar_archivo, name = "descargar")
]