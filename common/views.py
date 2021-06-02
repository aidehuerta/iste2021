from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def description(request):
    return render(request, 'description.html')


@login_required
def home(request):
    return render(request, 'home.html')
