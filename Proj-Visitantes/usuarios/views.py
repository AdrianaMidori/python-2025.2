from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'descricao' : 'Ligando frontend com backend'
    }
    return render(request, "index.html", context)