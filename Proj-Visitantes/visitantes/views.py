from django.shortcuts import render

def registrar_visitante(request):
    context = {}
    return render(request, "cadastro_visitante.html", context)
