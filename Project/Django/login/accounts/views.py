from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})