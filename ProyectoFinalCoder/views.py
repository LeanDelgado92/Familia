from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from ProyectoFinalCoder.models import Post, Mensaje 
from ProyectoFinalCoder.forms import UsuarioForm
from ProyectoFinalCoder.models import Avatar
from django.contrib.auth.admin import User


def index (recuest):
    return render (recuest, "ProyectoFinalCoder/index.html",)

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post
    
class PostCrear (CreateView):
    model = Post
    sucess_url = reverse_lazy("ProyectoFinalCoder-Listar")
    fields = '__all__'

class PostBorrar (LoginRequiredMixin, DeleteView):
    model = Post
    sucess_url = reverse_lazy("ProyectoFinalCoder-Borrar")
    
class PostActualizar (LoginRequiredMixin, UpdateView):
    model = Post
    sucess_url = reverse_lazy("ProyectoFinalCoder-Actualizar")
    fields = "__all__"
    
class UserSignUp (CreateView):
    form_class = UsuarioForm
    template_name = 'Registration/signup.html'
    sucess_url = reverse_lazy ("ProyectoFinalCoder-SignUp")
    
class UserLogin (LoginView):
    next_page = reverse_lazy ("ProyectoFinalCoder-Listar")
    
class UserLogout (LogoutView):
    next_page = reverse_lazy ("ProyectoFinalCoder-index")
    
class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("ProyectoFinalCoder-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("ProyectoFinalCoder-mensajes-listar")

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('ProyectoFinalCoder-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('ProyectoFinalCoder-listar')