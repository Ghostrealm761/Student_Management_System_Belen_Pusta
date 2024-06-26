from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



from .models import Student
from .forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })


def view_student(request, id):
    return HttpResponseRedirect(reverse('index'))
    
def add(request):
    if request.method == 'POST':
      form = StudentForm(request.POST)
      if form.is_valid():
        new_first_name = form.cleaned_data['first_name']
        new_last_name = form.cleaned_data['last_name']
        new_course = form.cleaned_data['course']
        new_grade = form.cleaned_data['grade']
        new_age = form.cleaned_data['age']
        
        new_student = Student(
          first_name = new_first_name,
          last_name = new_last_name,
          course = new_course,
          grade = new_grade,
          age = new_age,
        )
        new_student.save()
        return render(request, 'students/add.html', {
          'form': StudentForm(),
          'success': True
        })
            
    else:
      form = StudentForm()
    return render(request, 'students/add.html', {
      'form': StudentForm()
    })
        
def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

