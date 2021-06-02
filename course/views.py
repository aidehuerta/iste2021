from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import CourseForm
from .models import Course


@login_required
def listing(request):
    context = {
        'course': Course.objects.all()
    }
    return render(request, 'list_course.html', context=context)


@login_required
def add(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('course:home'))

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Successfully added course!')
            return redirect(reverse('course:home'))
        else:
            messages.error(
                request, 'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()

    context = {
        'form': form
    }
    return render(request, 'add_course.html', context)


@login_required
def edit(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('course:home'))

    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course!')
            return redirect(reverse('course:home'))
        else:
            messages.error(
                request, 'Failed to update course. Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.title}')

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'edit_course.html', context)


@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('course:home'))

    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, 'Course deleted!')
    return redirect(reverse('course:home'))
