from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render, reverse

from session.models import Emotion, Session

from .forms import ContentForm
from .models import Content


@login_required
def home(request):
    if not request.user.has_perm('content.view_content'):
        messages.error(request, 'No tienes el permiso para ver contenidos.')
        return redirect(reverse('common:home'))

    context = {
        'content': Content.objects.all()
    }

    return render(request, 'content/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('content.add_content'):
        messages.error(
            request, 'No tienes el permiso para agregar contenidos.')
        return redirect(reverse('content:home'))

    if request.method == 'POST':
        form = ContentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego el contenido "{form.cleaned_data.get("title")}" con éxito.')
            return redirect(reverse('content:home'))

        else:
            messages.error(
                request, 'No se pudo agregar el contenido. Por favor revisa los datos.')

    else:
        form = ContentForm()

    context = {
        'form': form
    }

    return render(request, 'content/add.html', context)


@login_required
def edit(request, pk):
    content = get_object_or_404(Content, pk=pk)

    if request.method == 'POST':
        if not request.user.has_perm('content.change_content'):
            messages.error(
                request, 'No tienes el permiso para editar contenidos.')
            return redirect(reverse('content:home'))

        form = ContentForm(request.POST, instance=content)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el contenido "{form.cleaned_data.get("title")}" con éxito.')
            return redirect(reverse('content:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar el contenido. Por favor revisa los datos.')

    else:
        form = ContentForm(instance=content)

    context = {
        'form': form,
        'content': content,
    }

    return render(request, 'content/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('content.delete_content'):
        messages.error(request, 'No tienes el permiso para borrar contenidos.')
        return redirect(reverse('content:home'))

    content = get_object_or_404(Content, pk=pk)

    try:
        content.delete()
        messages.success(
            request, f'El contenido "{content.title}" fue eliminado.')

    except:
        messages.error(
            request, f'El contenido "{content.title}" no se pudo borrar, tiene sesiones.')

    return redirect(reverse('content:home'))


@login_required
def report(request, pk):
    if not request.user.has_perm('content.view_content'):
        messages.error(request, 'No tienes el permiso para ver contenidos.')
        return redirect(reverse('common:home'))

    content = get_object_or_404(Content, pk=pk)
    sessions = Session.objects.filter(
        content=content
    ).values(
        'emotion__name',
        'emotion__color'
    ).annotate(
        sum=Sum('emotion')
    )

    labels = []
    colors = []
    data = []
    if sessions.exists():
        labels = [_['emotion__name'] for _ in sessions]
        colors = [_['emotion__color'] for _ in sessions]
        data = [_['sum'] for _ in sessions]

    context = {
        'content': content,
        'labels': labels,
        'colors': colors,
        'data': data,
    }

    return render(request, 'content/report.html', context=context)
