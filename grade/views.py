from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import GradeForm
from .models import Grade


@login_required
def home(request):
    if not request.user.has_perm('grade.view_grade'):
        messages.error(request, 'No tienes el permiso para ver los grados.')
        return redirect(reverse('common:home'))

    context = {
        'grade': Grade.objects.all()
    }

    return render(request, 'grade/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('grade.add_grade'):
        messages.error(
            request, 'No tienes el permiso para agregar grados.')
        return redirect(reverse('grade:home'))

    if request.method == 'POST':
        form = GradeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego el grado "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('grade:home'))

        else:
            messages.error(
                request, 'No se pudo agregar el grado. Por favor revisa los datos.')

    else:
        form = GradeForm()

    context = {
        'form': form
    }

    return render(request, 'grade/add.html', context)


@login_required
def edit(request, pk):
    if not request.user.has_perm('grade.change_grade'):
        messages.error(request, 'No tienes el permiso para editar los grados.')
        return redirect(reverse('grade:home'))

    grade = get_object_or_404(Grade, pk=pk)

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el contenido "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('grade:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar el grado. Por favor revisa los datos.')

    else:
        form = GradeForm(instance=grade)

    context = {
        'form': form,
        'grade': grade,
    }

    return render(request, 'grade/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('grade.delete_grade'):
        messages.error(request, 'No tienes el permiso para borrar grados.')
        return redirect(reverse('grade:home'))

    grade = get_object_or_404(Grade, pk=pk)
    grade.delete()
    messages.success(request, f'El grado "{grade.name}" fue eliminado.')

    return redirect(reverse('grade:home'))
