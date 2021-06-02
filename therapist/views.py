from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import TherapistForm
from .models import Therapist


@login_required
def listing(request):
    context = {
        'therapist': Therapist.objects.all()
    }
    return render(request, 'list_therapist.html', context=context)


@login_required
def add(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('therapist:home'))

    if request.method == 'POST':
        form = eacherForm(request.POST)
        if form.is_valid():
            therapist = form.save()
            messages.success(request, 'Successfully added therapist!')
            return redirect(reverse('therapist:home'))
        else:
            messages.error(
                request, 'Failed to add therapist. Please ensure the form is valid.')
    else:
        form = TherapistForm()

    context = {
        'form': form
    }
    return render(request, 'add_therapist.html', context)


@login_required
def edit(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('therapist:home'))

    therapist = get_object_or_404(Therapist, pk=pk)

    if request.method == 'POST':
        form = TherapistForm(request.POST, instance=therapist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated therapist!')
            return redirect(reverse('therapist:home'))
        else:
            messages.error(
                request, 'Failed to update therapist. Please ensure the form is valid.')
    else:
        form = TherapistForm(instance=therapist)
        messages.info(request, f'You are editing {therapist.title}')

    context = {
        'form': form,
        'therapist': therapist,
    }
    return render(request, 'edit_therapist.html', context)


@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('therapist:home'))

    therapist = get_object_or_404(Therapist, pk=pk)
    therapist.delete()
    messages.success(request, 'therapist deleted!')
    return redirect(reverse('therapist:home'))
