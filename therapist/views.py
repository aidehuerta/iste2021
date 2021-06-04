from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import TherapistForm
from .models import Therapist


@login_required
def home(request):
    if not request.user.has_perm('therapist.view_therapist'):
        messages.error(request, 'No tienes el permiso para ver terapeutas.')
        return redirect(reverse('common:home'))

    context = {
        'therapist': Therapist.objects.all()
    }

    return render(request, 'therapist/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('therapist.add_therapist'):
        messages.error(
            request, 'No tienes el permiso para agregar terapeutas.')
        return redirect(reverse('therapist:home'))

    if request.method == 'POST':
        form = TherapistForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego el terapeuta "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('therapist:home'))

        else:
            messages.error(
                request, 'No se pudo agregar el terapeuta. Por favor revisa los datos.')

    else:
        form = TherapistForm()

    context = {
        'form': form
    }

    return render(request, 'therapist/add.html', context)


@login_required
def edit(request, pk):
    if not request.user.has_perm('therapist.change_therapist'):
        messages.error(request, 'No tienes el permiso para editar terapeutas.')
        return redirect(reverse('therapist:home'))

    therapist = get_object_or_404(Therapist, pk=pk)

    if request.method == 'POST':
        form = TherapistForm(request.POST, instance=therapist)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el terapeuta "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('therapist:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar el terapeuta. Por favor revisa los datos.')

    else:
        form = TherapistForm(instance=therapist)

    context = {
        'form': form,
        'therapist': therapist,
    }

    return render(request, 'therapist/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('therapist.delete_therapist'):
        messages.error(request, 'No tienes el permiso para borrar terapeutas.')
        return redirect(reverse('therapist:home'))

    therapist = get_object_or_404(Therapist, pk=pk)
    therapist.delete()
    messages.success(
        request, f'El terapeuta "{therapist.name}" fue eliminado.')

    return redirect(reverse('therapist:home'))
