from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import signup, contact
from .models import Contact, Product
from django.views.generic import ListView, DetailView, CreateView

class home(ListView):
    model = Product
    template_name = 'home.html'

class product(ListView):
    model = Product
    template_name = 'product.html'

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')

class contact(CreateView):
    model = Contact
    form_class = contact
    template_name = 'contact.html'
    success_url = reverse_lazy('success')

class detail(DetailView):
    model = Product
    template_name = 'detail.html'

class register(generic.CreateView):
    form_class = signup
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')