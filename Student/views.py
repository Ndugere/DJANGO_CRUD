from django.shortcuts import render
from .models import Stud

# Create your views here.
def index(request):
    
    return render(request, 'students/index.html', {
        "students" : Stud.objects.all()
    })
def student_view(request, id):
    student = Stud.objects.get(pk=id)
    return render(request, "students/view.html", {
        "student": student
    })