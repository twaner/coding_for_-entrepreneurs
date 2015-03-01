# imports
from django.shortcuts import render

# views


def home(request):
    context = {}
    template = "home.html"
    return render(request, template, context)