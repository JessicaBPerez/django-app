from django.shortcuts import render, redirect
from .models import School, Professor
from .forms import SchoolForm, ProfessorForm

# Create your views here.


def school_index(request):
    context = {'schools': School.objects.all()}
    return render(request, 'todo/school_index.html', context)


def professor_index(request):
    context = {'professors': Professor.objects.all()}
    return render(request, 'todo/professor_index.html', context)

# To actually view Individuals


def school_show(request, id):
    context = {'school': School.objects.get(id=id)}
    return render(request, 'todo/school_show.html', context)


def professor_show(request, id):
    context = {'professor': Professor.objects.get(id=id)}
    return render(request, 'todo/professor_show.html', context)


def school_new(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save()
            # Had to fix from 'school_index' to 'school_show'
            return redirect('school_show', id=school.id)
    else:
        form = SchoolForm()
        return render(request, 'todo/school_form.html', {'form': form})


def professor_new(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save()
            # Had to fix from 'school_index' to 'school_show'
            return redirect('professor_show', id=professor.id)
    else:
        form = ProfessorForm()
        return render(request, 'todo/professor_form.html', {'form': form})

# Edit


def school_edit(request, id):
    school = School.objects.get(id=id)
    if request.method == "POST":
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            school = form.save()
            return redirect('school_show', id=school.id)
    else:
        form = SchoolForm(instance=school)
        return render(request, 'todo/school_form.html', {'form': form})


def professor_edit(request, id):
    professor = Professor.objects.get(id=id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            professor = form.save()
            return redirect('professor_show', id=professor.id)
    else:
        form = ProfessorForm(instance=professor)
        return render(request, 'todo/professor_form.html', {'form': form})

# Delete


def school_delete(request, id):
    # School.objects.get(id=id).delete()
    # return redirect('school_index')
    if request.method == 'POST':
        School.objects.get(id=id).delete()
    return redirect('school_index')


def professor_delete(request, id):
    # School.objects.get(id=id).delete()
    # return redirect('school_index')
    if request.method == 'POST':
        Professor.objects.get(id=id).delete()
    return redirect('professor_index')
