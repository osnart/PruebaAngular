from django.shortcuts import render, redirect
from horario_sala.foms import HorarioSalaForm
from horario_sala.models import HoraSala
from django.views.generic import ListView


# Create your views here.
class IndexHorarioSala(ListView):
    template_name = 'index.html'
    context_object_name = 'lista_horarios_sala'

    def  get_queryset(self):
        return HoraSala.objects.all()


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
        
def create_asistencia(request):
    if request.method == 'POST':
        form = HorarioSalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = HorarioSalaForm()
    return render(request, 'create.html', {'form':form})  

def delete_asistencia(request, id):
    horario = HoraSala.objects.get(id = id)
    horario.delete()
    return redirect('index')

def edit_asistencia(request , id):
    horario = HoraSala.objects.get( id=id)
    return render(request, 'edit.html' , {'horario' :horario})

def update_asistencia (request , id):
    horario = HoraSala.objects.get( id=id)
    form = HorarioSalaForm(request.POST, instance = horario)
    if form.is_valid():
        form.save()
        return redirect( "index" )
    return render(request, 'edit.html' , {'horario' : horario})


            