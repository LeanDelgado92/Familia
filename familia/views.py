from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView 
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from familia.models import Familiar
from familia.forms import Buscar, FamiliarForm


def index(request):
    return render(request, "Familia/saludar.html")

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "Familia/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'familia/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
    
class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'familia/actualizar_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
    def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  
    def post(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST ,instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
        return render(request, self.template_name, {"form": form})
 
class AltaFamiliar(View):
    
    form_class = FamiliarForm
    template_name = 'familia/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class FamiliarDetalle (DetailView) :
    model = Familiar
    
class FamiliarList(ListView):
    model = Familiar
    
class FamiliarCrear(CreateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte"]
    
class FamiliarBorrar(DeleteView):
    model = Familiar
    success_url = "/panel-familia"
    
class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte"]
    

