#Exemplo de Herança

class Animal():
    def __init__(self):
        print('Animal Criado')
    
    def quemSouEu(self):
        print('Eu sou um animal')

    def comer(self):
        print('Comendo...')

class Cachorro(Animal):
    def quemSouEu(self):
        print('Eu sou um cachorro')

class Jacare(Animal):
    def nadar(self):
        print('Nadando...')

