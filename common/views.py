from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'common/index.html')


def description(request):
    return render(request, 'common/description.html')


@login_required
def home(request):
    return render(request, 'common/home.html')
