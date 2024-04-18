from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Butterfly, Flora
from .forms import CycleForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def butterflies_index(request):
  butterflies = Butterfly.objects.all()
  return render(request, 'butterflies/index.html', {
    'butterflies': butterflies
  })


def butterflies_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  id_list = butterfly.floras.all().values_list('id')
  floras_butterfly_doesnt_have = Flora.objects.exclude(id__in=id_list)
  cycle_form = CycleForm()
  return render(request, 'butterflies/detail.html', {
    'butterfly': butterfly, 'cycle_form': cycle_form,
    'floras': floras_butterfly_doesnt_have
  })



def add_feeding(request, butterfly_id):
  form = CycleForm(request.POST)
  if form.is_valid():
    new_cycle = form.save(commit=False)
    new_cycle.butterfly_id = butterfly_id
    new_cycle.save()
  return redirect('detail', butterfly_id=butterfly_id)

class ButterflyCreate(CreateView):
  model = Butterfly
  fields = ['name', 'scientific', 'description', 'size']

class ButterflyUpdate(UpdateView):
  model = Butterfly
  fields = ['scientific', 'description', 'size']

class ButterflyDelete(DeleteView):
  model = Butterfly
  success_url = '/butterflies'



class FloraList(ListView):
  model = Flora

class FloraDetail(DetailView):
  model = Flora

class FloraCreate(CreateView):
  model = Flora
  fields = '__all__'

class FloraUpdate(UpdateView):
  model = Flora
  fields = ['name', 'color']

class FloraDelete(DeleteView):
  model = Flora
  success_url = '/floras'

def assoc_flora(request, butterfly_id, flora_id):
  Butterfly.objects.get(id=butterfly_id).floras.add(flora_id)
  return redirect('detail', butterfly_id=butterfly_id)

def unassoc_flora(request, butterfly_id, flora_id):
  Butterfly.objects.get(id=butterfly_id).floras.remove(flora_id)
  return redirect('detail', butterfly_id=butterfly_id)