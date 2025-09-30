<<<<<<< HEAD
"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
=======
>>>>>>> 7affcdca35c7b272664d64d51c9db9b76726bed8
from django.contrib import admin
from django.urls import path
from index.views import index

from index.views import index
from index.views import contato_bs
from index.views import imagens_bs
from index.views import locais_bs
from index.views import sobre_bs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]

urlpatterns += [
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('contato_bs.html', contato_bs, name='contato_bs'),
    path('imagens_bs.html', imagens_bs, name='imagens_bs'),
    path('locais_bs.html', locais_bs, name='locais_bs'),
    path('sobre_bs.html', sobre_bs, name='sobre_bs')
]
