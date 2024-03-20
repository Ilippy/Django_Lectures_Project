from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    logger.info("Index page accessed")
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('<h1>Oops, something went wrong</h1>')
    else:
        logger.debug('About page accessed')
        return HttpResponse("<h1>This is the about page</h1>")
