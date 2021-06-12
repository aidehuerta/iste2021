from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import DiagnosisForm
from .models import Diagnosis


@login_required
def home(request):
    if not request.user.has_perm('diagnosis.view_diagnosis'):
        messages.error(request, 'No tienes el permiso para ver diagnósticos.')
        return redirect(reverse('common:home'))

    context = {
        'diagnosis': Diagnosis.objects.all()
    }

    return render(request, 'diagnosis/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('diagnosis.add_diagnosis'):
        messages.error(
            request, 'No tienes el permiso para agregar diagnósticos.')
        return redirect(reverse('diagnosis:home'))

    if request.method == 'POST':
        form = DiagnosisForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego el diagnóstico "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('diagnosis:home'))

        else:
            messages.error(
                request, 'No se pudo agregar el diagnóstico. Por favor revisa los datos.')

    else:
        form = DiagnosisForm()

    context = {
        'form': form
    }

    return render(request, 'diagnosis/add.html', context)


@login_required
def edit(request, pk):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)

    if request.method == 'POST':
        if not request.user.has_perm('diagnosis.change_diagnosis'):
            messages.error(
                request, 'No tienes el permiso para editar diagnósticos.')
            return redirect(reverse('diagnosis:home'))

        form = DiagnosisForm(request.POST, instance=diagnosis)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el diagnóstico "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('diagnosis:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar el contenido. Por favor revisa los datos.')

    else:
        form = DiagnosisForm(instance=diagnosis)

    context = {
        'form': form,
        'diagnosis': diagnosis,
    }

    return render(request, 'diagnosis/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('diagnosis.delete_diagnosis'):
        messages.error(
            request, 'No tienes el permiso para borrar diagnósticos.')
        return redirect(reverse('diagnosis:home'))

    diagnosis = get_object_or_404(Diagnosis, pk=pk)

    try:
        diagnosis.delete()
        messages.success(
            request, f'El diagnóstico "{diagnosis.name}" fue eliminado.')

    except:
        messages.error(
            request, f'El diagnóstico "{diagnosis.name}" no se pudo borrar, vinculado a estudiantes.')

    return redirect(reverse('diagnosis:home'))
