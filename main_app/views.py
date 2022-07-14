from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Exchange, Wallet

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ExchangeIndex(ListView):
    model = Exchange
    template_name = 'exchanges/index.html'

class ExchangeDetail(DetailView):
    model = Exchange
    template_name = 'exchanges/detail.html'

class ExchangeCreate(LoginRequiredMixin, CreateView):
    model = Exchange
    fields = ['name', 'description', 'link']
    success_url = '/exchanges/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExchangeUpdate(LoginRequiredMixin, UpdateView):
    model = Exchange
    fields = ['name', 'description', 'link']

class ExchangeDelete(LoginRequiredMixin, DeleteView):
    model = Exchange
    success_url = '/exchanges/'

class WalletIndex(ListView):
    model = Wallet
    template_name = 'wallets/index.html'

class WalletDetail(DetailView):
    model = Wallet
    template_name = 'wallets/detail.html'

class WalletCreate(LoginRequiredMixin, CreateView):
    model = Wallet
    fields = ['name', 'description', 'link']

class WalletUpdate(LoginRequiredMixin, UpdateView):
    model = Wallet
    fields = ['name', 'description', 'link']

class WalletDelete(LoginRequiredMixin, DeleteView):
    model = Wallet
    success_url = '/wallets'