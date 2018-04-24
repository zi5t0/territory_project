from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from territory_project.models import Territorio


def show_list(request):
    territorios = Territorio.objects.all()
    return render(request, 'territorios/list.html', {'territorios': territorios})


def show_edit(request):
    id = request.GET.get('id', 0)
    territory_data = {}
    accion = "Crear"
    if Territorio.objects.filter(id=id).exists():
        territorio = Territorio.objects.get(id=id)
        territory_data = {
            'id': str(territorio.id),
            'numero': str(territorio.numero),
            'campania': str(territorio.campania),
            'lluvia': str(territorio.lluvia),
            'zona': str(territorio.zona),
            'estado': str(territorio.estado),
        }
        accion = "Editar"
    return render(request, 'territorios/edit.html', {'data': territory_data, 'accion': accion})


def handle_edit(request):
    id = request.POST.get('id', '')
    campania = 0
    lluvia = 0
    if request.POST.get('campania'):
        campania = 1
    if request.POST.get('lluvia'):
        lluvia = 1
    if id:
        territorio = Territorio.objects.filter(id=id).update(numero = request.POST.get('numero'),
                                                          campania = campania,
                                                          lluvia = lluvia,
                                                          zona = request.POST.get('zona'))
    else:
        territorio = Territorio.objects.create(numero = request.POST.get('numero'),
                                               campania = campania,
                                               lluvia = lluvia,
                                               zona = request.POST.get('zona'))

    return redirect('/territorios/')


def handle_delete(request):
    id = request.GET.get('id')
    try:
        Territorio.objects.get(id=id).delete()
    except:
        messages.error(request, 'Error al eliminar: {0}'.format(e))
    return redirect('/territorios/')
