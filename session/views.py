from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import SessionForm
from .models import Session


@login_required
def listing(request):
    context = {
        'session': Session.objects.all()
    }
    return render(request, 'list_session.html', context=context)


@login_required
def add(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('session:home'))

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            messages.success(request, 'Successfully added session!')
            return redirect(reverse('session:home'))
        else:
            messages.error(
                request, 'Failed to add session. Please ensure the form is valid.')
    else:
        form = SessionForm()

    context = {
        'form': form
    }
    return render(request, 'add_session.html', context)


@login_required
def edit(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('session:home'))

    session = get_object_or_404(Session, pk=pk)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated session!')
            return redirect(reverse('session:home'))
        else:
            messages.error(
                request, 'Failed to update session. Please ensure the form is valid.')
    else:
        form = SessionForm(instance=session)
        messages.info(request, f'You are editing {session.title}')

    context = {
        'form': form,
        'session': session,
    }
    return render(request, 'edit_session.html', context)


@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('session:home'))

    session = get_object_or_404(Session, pk=pk)
    session.delete()
    messages.success(request, 'Session deleted!')
    return redirect(reverse('session:home'))
