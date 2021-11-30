""" Views """

from django.http import HttpResponse

# Utilities
from datetime import datetime


def hi(request):
    """Return a greeting"""
    return HttpResponse('Oh, hi Jaiden! Current server time is {now}'.format(
        now=datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    ))


def hello(request):
    """Return a greeting"""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f'Oh, hi Jaiden! Current server time is {now}')


def debugger(request):
    import pdb;
    pdb.set_trace()
    return HttpResponse('Oh, hi!')


def list_numbers(request):
    # Pass numbers into URL: list_numbers/?numbers=7,14,21,28
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))
