from django.shortcuts import redirect, render
from .models import Note

def wall(request):
    notes = Note.objects.all()
    return render(request, 'to_do/wall.html', {'notes': notes} )

def add(request):
    if request.method == 'POST':
        new_note = Note(
            title = request.POST['title'],
            text = request.POST['text']
        )

        new_note.save()
        return redirect( 'wall' )

    return render(request, 'to_do/add.html')


# Create your views here.
