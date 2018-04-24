from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import utils


def show_login(request):
    if request.user.is_authenticated:
        return redirect('/inicio/')
    else:
        return render(request, 'login/login.html')


def show_login_error(request, error):
    messages.error(request, error)
    return render(request, 'login/login.html')


def show_index(request):
    return render(request, 'index.html')


def handle_login(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')

    try:
        user = utils.handle_auth(request, name, password)
        if user is not None:
            return redirect('/inicio/')
        else:
            return redirect('/')
    except Exception as e:
        error = str(e)
        return show_login_error(request, error)


def handle_logout(request):
    logout(request)
    return render(request, 'login/login.html')


# Function that redirect user to a Forbidden message template
def redirect_forbidden(request):
    return render(request, 'forbidden.html')


def show_404(request):
    return render(request, '404.html')


def show_500(request):
    return render(request, '500.html')