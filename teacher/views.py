from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import TeacherForm
from .models import Teacher


@login_required
def listing(request):
    context = {
        'teacher': Teacher.objects.all()
    }
    return render(request, 'list_teacher.html', context=context)


@login_required
def add(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('teacher:home'))

    if request.method == 'POST':
        form = eacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            messages.success(request, 'Successfully added teacher!')
            return redirect(reverse('teacher:home'))
        else:
            messages.error(
                request, 'Failed to add teacher. Please ensure the form is valid.')
    else:
        form = TeacherForm()

    context = {
        'form': form
    }
    return render(request, 'add_teacher.html', context)


@login_required
def edit(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('teacher:home'))

    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated teacher!')
            return redirect(reverse('teacher:home'))
        else:
            messages.error(
                request, 'Failed to update teacher. Please ensure the form is valid.')
    else:
        form = TeacherForm(instance=teacher)
        messages.info(request, f'You are editing {teacher.title}')

    context = {
        'form': form,
        'teacher': teacher,
    }
    return render(request, 'edit_teacher.html', context)


@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('teacher:home'))

    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    messages.success(request, 'Teacher deleted!')
    return redirect(reverse('teacher:home'))
