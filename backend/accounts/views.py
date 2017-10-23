import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import ServiceProvider, CustomUser
from jobs.models import Job

def provider_page(request, pk):
    provider = get_object_or_404(CustomUser, pk=pk)
    jobs = Job.objects.filter(provider=provider)
    return render(request, 'provider_page.html', {'provider': provider, 'jobs': jobs})

def login_view(request):
    if request.method == "GET":
        print(request.GET, flush=True)
        username = request.GET.get('username')
        print (username, flush=True)
        password = request.GET.get('password')
        print (password, flush=True)
        user = authenticate(username=username, password=password)
        if user is None:
            data = {"is_authed": False, 'username':username}
        else:
            login(request, user)
            data = {
                "is_authed": True,
                "username": username
            }
        return JsonResponse(data)


def signup_view(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    password_confirmation = request.GET.get('password_confirmation')
    form = UserCreationForm(username=username, password1=password, password2=password_confirmation)
    if form.is_valid():
        user = form.save()
        login(request, user)
        data = {
            "is_authed": True,
            "username": username
        }
    return JsonResponse(data)

def logout_view(request):
    logout(request)
# Create your views here.
