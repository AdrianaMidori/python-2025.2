from django.shortcuts import render, get_object_or_404
from visitantes.forms import VisitanteForm
from visitantes.models import Visitante

def registrar_visitante(request):
    form = VisitanteForm()

    context = {
        "nome_pagina" : "Registrar Visitante",
        "form" : form
    }
    return render(request, "registrar_visitante.html", context)


def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitante, id=id)
    context = {
        "nome_pagina" : "Informações do Visitante",
        "visitante" : visitante
    }
    


    return render(request, "informacoes_visitante.html", context)