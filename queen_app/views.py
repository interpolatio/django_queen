from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic


def index(request):
    if (request.GET.get('work')):
        print("button")
    return render(request, 'queen_app/detail.html')
