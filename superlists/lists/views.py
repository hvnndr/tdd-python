from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    page = '<html><title>To-Do lists</title></html>'
    response = HttpResponse(page)
    print(type(response.content))
    return response


def second_page():
    return 'segunda pagina'
