from session.serializers import SessionSerializer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from rest_framework import generics, status
from rest_framework.response import Response

from .forms import SessionForm
from .models import Session


@login_required
def home(request):
    if not request.user.has_perm('session.view_session'):
        messages.error(request, 'No tienes el permiso para ver las sesiones.')
        return redirect(reverse('common:home'))

    context = {
        'session': Session.objects.all()
    }

    return render(request, 'session/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('session.add_session'):
        messages.error(
            request, 'No tienes el permiso para agregar sesiones.')
        return redirect(reverse('session:home'))

    if request.method == 'POST':
        form = SessionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se agrego la sesión "{form.cleaned_data.get("student")} - {form.cleaned_data.get("content")}" con éxito.')
            return redirect(reverse('session:home'))

        else:
            messages.error(
                request, 'No se pudo agregar la sesión. Por favor revisa los datos.')

    else:
        form = SessionForm()

    context = {
        'form': form
    }

    return render(request, 'session/add.html', context)


@login_required
def edit(request, pk):
    if not request.user.has_perm('session.change_session'):
        messages.error(request, 'No tienes el permiso para editar la sesión.')
        return redirect(reverse('session:home'))

    session = get_object_or_404(Session, pk=pk)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Se edito el contenido "{form.cleaned_data.get("student")} - {form.cleaned_data.get("content")}" con éxito.')
            return redirect(reverse('session:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar la sesión. Por favor revisa los datos.')

    else:
        form = SessionForm(instance=session)

    context = {
        'form': form,
        'session': session,
    }

    return render(request, 'session/edit.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('session.delete_session'):
        messages.error(request, 'No tienes el permiso para borrar sesiones.')
        return redirect(reverse('session:home'))

    session = get_object_or_404(Session, pk=pk)
    session.delete()
    messages.success(
        request, f'La sesión "{session.student} - {session.content}" fue eliminado.')

    return redirect(reverse('session:home'))


class SetButton(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        colores = {
            '1': 'Verde',
            '2': 'Azul',
            '3': 'Rojo',
            '4': 'Amarillo',
            '5': 'Blanco',
        }

        boton = self.request.query_params.get('boton')

        sesion = Session.objects.filter(
            emotion__isnull=True
        ).order_by(
            '-id'
        ).first()

        respuesta = ''
        if sesion is not None:
            sesion.emotion_id = int(boton)
            sesion.save()
            respuesta = f'Sesión {sesion}. '

        else:
            respuesta = 'No hay sesión esperando emoción. '

        respuesta += colores.get(boton, 'El color no es reconocido.')

        print(boton, respuesta)

        return Response(f'----{respuesta}-----', status=status.HTTP_200_OK)
