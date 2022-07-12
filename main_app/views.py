from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView 
from .models import Exchange, Wallet

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ExchangeIndex(ListView):
    model = Exchange
    template_name = 'exchanges/index.html'

class ExchangeDetail(DetailView):
    model = Exchange
    template_name = 'exchanges/detail.html'

class WalletIndex(ListView):
    model = Wallet
    template_name = 'wallets/index.html'

class WalletDetail(DetailView):
    model = Wallet
    template_name = 'wallets/detail.html'