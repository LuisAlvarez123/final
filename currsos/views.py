from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
#from django.view.generic import CreateView

from .models import Asignacion
from .forms import AsignacionForm

class AsignacionView(LoginRequiredMixin, generic.ListView):
    model = Asignacion
    template_name = 'app/alumn_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AsignacionNew(LoginRequiredMixin, generic.CreateView):
    model = Asignacion
    template_name = "app/alum_form.html"
    context_object_name = "obj"
    form_class = AsignacionForm
    success_url = reverse_lazy("app:alumn_list")
    login_url = 'app:login'

class AsignacionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Asignacion
    template_name = "app/alum_form.html"
    context_object_name = "obj"
    form_class = AsignacionForm
    success_url = reverse_lazy("app:alumn_list")
    login_url = 'app:login'

class AsignacionDel(LoginRequiredMixin, generic.DeleteView):
    model = Asignacion
    template_name = "app/catalogo_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("app:alumn_list")