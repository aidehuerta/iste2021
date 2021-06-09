from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('common:home'))
    else:
        return render(request, 'common/index.html')


def description(request):
    if request.user.is_authenticated:
        return redirect(reverse('common:home'))
    else:
        return render(request, 'common/description.html')


@login_required
def home(request):
    return render(request, 'common/home.html')
