from django.shortcuts import redirect, render
from .models import Note
from .forms import *

def wall(request):

    if request.method == 'POST':
       form = NoteForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect( '/' )

    notes = Note.objects.all()
    form = NoteForm()
    context = {'notes': notes, 'form': form}
    return render(request, 'to_do/wall.html', context)






# Create your views here.
