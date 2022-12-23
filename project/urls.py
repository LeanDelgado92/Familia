from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from familia.views import index
from familia.views import mostrar_familiares
from familia.views import BuscarFamiliar
from familia.views import AltaFamiliar
from familia.views import ActualizarFamiliar
from familia.views import FamiliarDetalle
from familia.views import FamiliarList
from familia.views import FamiliarCrear
from familia.views import FamiliarBorrar
from familia.views import FamiliarActualizar
from ProyectoFinalCoder.views import (index, PostListar, PostCrear, 
                                      PostDetalle, PostBorrar, PostActualizar, 
                                      UserSignUp, UserLogin, UserLogout,
                                      MensajeDetalle, MensajeListar, MensajeCrear, MensajeBorrar,
                                    UserActualizar, AvatarActualizar)
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('familiares/', mostrar_familiares),
    path('familiares/buscar',BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('ProyectoFinalCoder/', index, name="ProyectoFinalCoder-Index"),
    path('ProyectoFinalCoder/listar/', PostListar.as_view(), name="ProyectoFinalCoder-Listar"),
    path('ProyectoFinalCoder/crear/', PostCrear.as_view(), name="ProyectoFinalCoder-Crear"),
    path('ProyectoFinalCoder/<int:pk>/detalle/', PostDetalle.as_view(), name="ProyectoFinalCoder-Detalle"),
    path('ProyectoFinalCoder/<int:pk>/borrar/', PostBorrar.as_view(), name="ProyectoFinalCoder-Borrar"),
    path('ProyectoFinalCoder/<int:pk>/actualizar/', PostActualizar.as_view(), name="ProyectoFinalCoder-Actualizar"),
    path('ProyectoFinalCoder/signup/', UserSignUp.as_view(), name= "ProyectoFinalCoder-SignUp"),
    path('ProyectoFinalCoder/login/', UserLogin.as_view(), name="ProyectoFinalCoder-Login"),
    path('ProyectoFinalCoder/logout/', UserLogout.as_view(), name="ProyectoFinalCoder-Logout"),
    path('ProyectoFinalCoder/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ProyectoFinalCoder-Mensajes-Detalle"),
    path('ProyectoFinalCoder/mensajes/listar/', MensajeListar.as_view(), name="ProyectoFinalCoder-Mensajes-Listar"),
    path('ProyectoFinalCoder/mensajes/crear/', MensajeCrear.as_view(), name="ProyectoFinalCoder-Mensajes-Crear"),
    path('ProyectoFinalCoder/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="ProyectoFinalCoder-Mensajes-Borrar"),
    path('ProyectoFinalCoder/about', TemplateView.as_view(template_name='ProyectoFinalCoder/about.html'), name="ProyectoFinalCoder-About"),
    path('ProyectoFinalCoder/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ProyectoFinalCoder-Users-Actualizar"),
    path('ProyectoFinalCoder/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ProyectoFinalCoder-Avatars-Actualizar"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)