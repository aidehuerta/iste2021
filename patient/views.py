from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import PatientForm
from .models import Patient


@login_required
def listing(request):
    context = {
        'patient': Patient.objects.all()
    }
    return render(request, 'list_patient.html', context=context)


@login_required
def add(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('patient:home'))

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, 'Successfully added patient!')
            return redirect(reverse('patient:home'))
        else:
            messages.error(
                request, 'Failed to add patient. Please ensure the form is valid.')
    else:
        form = PatientForm()

    context = {
        'form': form
    }
    return render(request, 'add_patient.html', context)


@login_required
def edit(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('patient:home'))

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated patient!')
            return redirect(reverse('patient:home'))
        else:
            messages.error(
                request, 'Failed to update patient. Please ensure the form is valid.')
    else:
        form = PatientForm(instance=patient)
        messages.info(request, f'You are editing {patient.title}')

    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'edit_patient.html', context)


@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('patient:home'))

    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    messages.success(request, 'Patient deleted!')
    return redirect(reverse('patient:home'))
