from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from apps.user.models import Usuario
from .forms import FormularioLogin, FormularioUsuario


class Login(FormView):
    template_name = 'user/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('todoapp:dashboard')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('')

class RegistroUsuario(CreateView):
    model = Usuario
    template_name="user/register.html"
    form_class = FormularioUsuario
    success_url = reverse_lazy('user:login')