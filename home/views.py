from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'home/index.html' ,{})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home:index')
    elif request.user.is_authenticated :
    	return redirect('home:index') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})	