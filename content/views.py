from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import ContentForm
from .models import Content


@login_required
def listing(request):
    context = {
        'content': Content.objects.all()
    }
    return render(request, 'list_content.html', context=context)


@login_required
def add(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('content:home'))

    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save()
            messages.success(request, 'Successfully added content!')
            return redirect(reverse('content:home'))
        else:
            messages.error(
                request, 'Failed to add content. Please ensure the form is valid.')
    else:
        form = ContentForm()

    context = {
        'form': form
    }
    return render(request, 'add_content.html', context)


@login_required
def edit(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('content:home'))

    content = get_object_or_404(Content, pk=pk)

    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated content!')
            return redirect(reverse('content:home'))
        else:
            messages.error(
                request, 'Failed to update content. Please ensure the form is valid.')
    else:
        form = ContentForm(instance=content)
        messages.info(request, f'You are editing {content.title}')

    context = {
        'form': form,
        'content': content,
    }
    return render(request, 'edit_content.html', context)


@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('content:home'))

    content = get_object_or_404(Content, pk=pk)
    content.delete()
    messages.success(request, 'Content deleted!')
    return redirect(reverse('content:home'))
