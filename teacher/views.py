from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import TeacherForm
from .models import Teacher


@login_required
def home(request):
    if not request.user.has_perm('teacher.view_teacher'):
        messages.error(request, 'No tienes el permiso para ver maestros.')
        return redirect(reverse('common:home'))

    context = {
        'teacher': Teacher.objects.all()
    }

    return render(request, 'teacher/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('teacher.add_teacher'):
        messages.error(
            request, 'No tienes el permiso para agregar maestros.')
        return redirect(reverse('teacher:home'))

    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego el maestro "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('teacher:home'))

        else:
            messages.error(
                request, 'No se pudo agregar el terapeuta. Por favor revisa los datos.')

    else:
        form = TeacherForm()

    context = {
        'form': form
    }

    return render(request, 'teacher/add.html', context)


@login_required
def edit(request, pk):
    if not request.user.has_perm('teacher.change_teacher'):
        messages.error(request, 'No tienes el permiso para editar maestros.')
        return redirect(reverse('teacher:home'))

    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el maestro "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('teacher:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar el maestro. Por favor revisa los datos.')

    else:
        form = TeacherForm(instance=teacher)

    context = {
        'form': form,
        'teacher': teacher,
    }

    return render(request, 'teacher/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('teacher.delete_teacher'):
        messages.error(request, 'No tienes el permiso para borrar maestros.')
        return redirect(reverse('teacher:home'))

    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    messages.success(request, f'El maestro "{teacher.name}" fue eliminado.')

    return redirect(reverse('teacher:home'))
