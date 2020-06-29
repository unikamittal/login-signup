from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Contact
import json
from django.http import HttpResponse

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')



def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        address = request.POST.get('desc', '')
        country = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, address=address, country=country)
        contact.save()
        confirm = True
        return render(request, 'contact.html', {'confirm': confirm})
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')