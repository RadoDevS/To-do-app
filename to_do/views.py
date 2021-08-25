from django.shortcuts import render

def wall(request):
    return render(request, 'to_do/wall.html' )
# Create your views here.
