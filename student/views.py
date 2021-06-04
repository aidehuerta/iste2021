from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import StudentForm
from .models import Student


@login_required
def home(request):
    if not request.user.has_perm('student.view_student'):
        messages.error(request, 'No tienes el permiso para ver estudiantes.')
        return redirect(reverse('common:home'))

    context = {
        'student': Student.objects.all()
    }

    return render(request, 'student/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('student.add_student'):
        messages.error(
            request, 'No tienes el permiso para agregar estudiantes.')
        return redirect(reverse('student:home'))

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego al estudiante "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('student:home'))

        else:
            messages.error(
                request, 'No se pudo agregar al estudiante. Por favor revisa los datos.')

    else:
        form = StudentForm()

    context = {
        'form': form
    }

    return render(request, 'student/add.html', context)


@login_required
def edit(request, pk):
    if not request.user.has_perm('student.change_student'):
        messages.error(
            request, 'No tienes el permiso para editar estudiantes.')
        return redirect(reverse('student:home'))

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito al estudiante "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('student:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar al estudiante. Por favor revisa los datos.')

    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
    }

    return render(request, 'student/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('student.delete_student'):
        messages.error(
            request, 'No tienes el permiso para borrar estudiantes.')
        return redirect(reverse('student:home'))

    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, f'El estudiante "{student.name}" fue eliminado.')
    return redirect(reverse('student:home'))
