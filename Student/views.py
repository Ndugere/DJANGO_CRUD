from django.shortcuts import render
from .models import Stud
from .forms import StudForm

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

def add(request):
    if request.method == "POST":
        form = StudForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Stud(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa,
            )
            new_student.save()
            
            return render(request, 'students/add.html', {
                'form': StudForm(),
                'success': True
            })
    else:
        form = StudForm()
    return render(request, 'students/add.html', { 
        'form': form 
    })
def edit(request, id):
    if request.method == "POST":
        student = Stud.objects.get(pk=id)
        form = StudForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Stud.objects.get(pk=id)
        form = StudForm(instance=student)
    return render(request, 'students/edit.html', {
        "form": form
    })