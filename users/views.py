from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')
    
    form = UserCreationForm
    context = {'form': form}
    return render(request, 'users/register.html', context)

# Create your views here.
