from django.shortcuts import render
from .models import Stud

# Create your views here.
def index(request):
    
    return render(request, 'students/index.html', {
        "students" : Stud.objects.all()
    })