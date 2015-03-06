# imports
from django.shortcuts import render

# views


def test_home(request):
    context = {}
    template = "donotuse.html"
    return render(request, template, context)