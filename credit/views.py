from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Client, Account, Credit


class IndexView(generic.ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'client_list'


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'detail.html'
    context_object_name = 'detail'
    pk_url_kwarg = 'id'




