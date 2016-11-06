from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import business, extendedUser

def index(request):
    return render(request, 'activity_graph/index.html')

#@login_required(login_url="login/")
def account(request):
    return render(request, 'activity_graph/account.html')

#@login_required(login_url="login/")
def feed (request):
    return render(request, 'activity_graph/feed.html')
