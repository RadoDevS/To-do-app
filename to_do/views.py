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


def update(request, pk):
    note = Note.objects.get(id = pk)
    form = NoteForm(instance=note)
    context = {'form': form}

    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note )
        if form.is_valid():
            form.save()
            return redirect( '/' )


    return render (request, 'to_do/update.html', context)


def delete(request, pk):
    item = Note.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item' : item}
    return render(request, 'to_do/delete.html', context)



# Create your views here.
