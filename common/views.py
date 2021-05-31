from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def description(request):
    return render(request, 'description.html')


def home(request):
    return render(request, 'home.html')
