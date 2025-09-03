# Primeira implementação

class Exemplo():
    pass

x = Exemplo()

# Segundo exemplo de classe
class Cachorro():
    def __init__(self):
        self.idade = 10
    
    def __str__(self):
        print('Eu sou um cachorro')

cachorro = Cachorro()

print(cachorro.idade)
