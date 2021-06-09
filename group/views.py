from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from common.models import Employee

from .forms import GroupForm
from .models import Group


@login_required
def home(request):
    if not request.user.has_perm('group.view_group'):
        messages.error(request, 'No tienes el permiso para ver los grupos.')
        return redirect(reverse('common:home'))

    employee = Employee.objects.filter(user=request.user).first()
    groups = Group.objects.all()
    if employee is not None and employee.department == 'DO':
        groups = groups.filter(user=request.user)

    context = {
        'group': groups
    }

    return render(request, 'group/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('group.add_group'):
        messages.error(
            request, 'No tienes el permiso para agregar grupos.')
        return redirect(reverse('group:home'))

    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego el grupo "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('group:home'))

        else:
            messages.error(
                request, 'No se pudo agregar el grupo. Por favor revisa los datos.')

    else:
        form = GroupForm()

    context = {
        'form': form
    }

    return render(request, 'group/add.html', context)


@login_required
def edit(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        if not request.user.has_perm('group.change_group'):
            messages.error(
                request, 'No tienes el permiso para editar los grupos.')
            return redirect(reverse('group:home'))

        form = GroupForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el grupo "{form.cleaned_data.get("name")}" con éxito.')
            return redirect(reverse('group:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar el grupo. Por favor revisa los datos.')

    else:
        form = GroupForm(instance=group)

    context = {
        'form': form,
        'group': group,
    }

    return render(request, 'group/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('group.delete_group'):
        messages.error(request, 'No tienes el permiso para borrar grupos.')
        return redirect(reverse('group:home'))

    group = get_object_or_404(Group, pk=pk)
    group.delete()
    messages.success(request, f'El grupo "{group.name}" fue eliminado.')

    return redirect(reverse('group:home'))
