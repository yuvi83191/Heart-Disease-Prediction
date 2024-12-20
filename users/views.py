from django.shortcuts import render,redirect
from.forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .models import Patient
from .forms import PatientForm
from django.http import HttpResponse
import csv

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number=form.cleaned_data.get('phone_number')
            dob=form.cleaned_data.get('dob')
            hospital_name=form.cleaned_data.get('hospital_name')
            profile = UserProfile(user=user,phone_number=phone_number,dob=dob,hospital_name=hospital_name)
            profile.save()
            login(request, user)
            return redirect('successfully_registered') 
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def successfully_registered(request):
    return render(request, "successfully_registered.html")


def patient_entry(request):
    return render(request, 'patient_entry.html')

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('successfully_logged_in')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required 
def successfully_logged_in(request):
    return render(request, 'successfully_logged_in.html')

def patient_entry(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('history') 
    else:
        form = PatientForm()
    
    return render(request, 'patient_entry.html', {'form': form})

def history(request):
    patients = Patient.objects.all()  
    return render(request, 'history.html', {'patients': patients})