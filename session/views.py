from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from rest_framework import generics, status
from rest_framework.response import Response

from common.models import Employee
from session.serializers import SessionSerializer

from .forms import SessionApplyForm, SessionForm
from .models import Session


@login_required
def home(request):
    if not request.user.has_perm('session.view_session'):
        messages.error(request, 'No tienes el permiso para ver las sesiones.')
        return redirect(reverse('common:home'))

    employee = Employee.objects.filter(user=request.user).first()
    sessions = Session.objects.all()
    if employee is not None and employee.department == 'DO':
        sessions = sessions.filter(user=request.user)

    context = {
        'session': sessions
    }

    return render(request, 'session/home.html', context=context)


@login_required
def add(request):
    if not request.user.has_perm('session.add_session'):
        messages.error(
            request, 'No tienes el permiso para agregar sesiones.')
        return redirect(reverse('session:home'))

    if request.method == 'POST':
        form = SessionForm(request.POST, user=request.user)

        if form.is_valid():
            if Session.objects.filter(
                    content=form.cleaned_data.get("content"),
                    user=form.cleaned_data.get("user")).exists():
                messages.error(
                    request, 'No se pudo agregar la sesión. Ya existe una para este estudiante y sesión.')
                return redirect(reverse('session:home'))

            form.save()
            messages.success(
                request, f'Se agrego la sesión "{form.cleaned_data.get("student")} - {form.cleaned_data.get("content")}" con éxito.')
            return redirect(reverse('session:apply', kwargs={'pk': form.instance.id}))

        else:
            messages.error(
                request, 'No se pudo agregar la sesión. Por favor revisa los datos.')

    else:
        form = SessionForm(user=request.user)

    context = {
        'form': form
    }

    return render(request, 'session/add.html', context)


@login_required
def edit(request, pk):
    session = get_object_or_404(Session, pk=pk)

    if request.method == 'POST':
        if not request.user.has_perm('session.change_session'):
            messages.error(
                request, 'No tienes el permiso para editar la sesión.')
            return redirect(reverse('session:home'))

        form = SessionForm(request.POST, instance=session, user=request.user)

        if form.is_valid():
            if Session.objects.filter(
                    content=form.cleaned_data.get("content"),
                    user=form.cleaned_data.get("user")
            ).exclude(
                id=session.id
            ).exists():
                messages.error(
                    request, 'No se pudo agregar la sesión. Ya existe una para este estudiante y sesión.')
                return redirect(reverse('session:home'))

            form.save()
            messages.success(
                request, f'Se edito el contenido "{form.cleaned_data.get("student")} - {form.cleaned_data.get("content")}" con éxito.')
            return redirect(reverse('session:home'))

        else:
            messages.error(
                request, 'No se pudo actualizar la sesión. Por favor revisa los datos.')

    else:
        form = SessionForm(instance=session, user=request.user)

    context = {
        'form': form,
        'session': session,
    }

    return render(request, 'session/edit.html', context)


@login_required
def apply(request, pk):
    session = get_object_or_404(Session, pk=pk)
    video_id = ''

    if session is not None:
        try:
            video_id = session.content.url.split('/')[-1]
        except:
            pass

    if request.method == 'POST':
        if not request.user.has_perm('session.change_session'):
            messages.error(
                request, 'No tienes el permiso para editar la sesión.')
            return redirect(reverse('session:home'))

        form = SessionApplyForm(request.POST, instance=session)

        if form.is_valid():
            messages.success(
                request, f'Se recibió la emoción para la sesión con éxito.')
            return redirect(reverse('session:edit', kwargs={'pk': form.instance.id}))

        else:
            messages.error(
                request, 'No se pudo actualizar la sesión. Por favor revisa los datos.')

    else:
        form = SessionApplyForm(instance=session)

    context = {
        'form': form,
        'session': session,
        'video_id': video_id,
    }

    return render(request, 'session/apply.html', context)


@login_required
def delete(request, pk):
    if not request.user.has_perm('session.delete_session'):
        messages.error(request, 'No tienes el permiso para borrar sesiones.')
        return redirect(reverse('session:home'))

    session = get_object_or_404(Session, pk=pk)

    try:
        session.delete()
        messages.success(
            request, f'La sesión "{session.student} - {session.content}" fue eliminado.')

    except:
        messages.error(
            request, f'El sesión "{session.student} - {session.content}" no se pudo borrar.')

    return redirect(reverse('session:home'))


class SetButton(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        colores = {
            '1': 'green',
            '2': 'blue',
            '3': 'red',
            '4': 'yellow',
            '5': 'white',
        }

        boton = kwargs.get('boton')
        if boton is None:
            boton = request.query_params.get('boton')

        if boton is not None:
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


class GetButton(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        session_id = kwargs.get('session_id')
        response = {
            'id': None,
            'color': ''
        }

        if session_id is not None:
            session_info = Session.objects.filter(
                id=session_id
            ).values(
                'emotion_id',
                'emotion__name',
            ).first()

            if session_info['emotion_id'] is not None:
                response = {
                    'id': session_info['emotion_id'],
                    'color': session_info['emotion__name']
                }

        return Response(response, status=status.HTTP_200_OK, content_type='application/json')
