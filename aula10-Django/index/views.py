<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   # return HttpResponse('Olá Mundo!')
    return render(request,'index.html')

def contato_bs(request):
    return render(request,'contato_bs.html')

def imagens_bs(request):
    return render(request,'imagens_bs.html')

def locais_bs(request):
    return render(request,'locais_bs.html')

def sobre_bs(request):
    return render(request,'sobre_bs.html')
=======
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá Mundo!!!')

>>>>>>> 7affcdca35c7b272664d64d51c9db9b76726bed8
