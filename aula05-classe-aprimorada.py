class Cachorro():
    def __init__(self, raca = 'Viralata'):
        self.raca = raca
        self.idade = 10
    
    def __str__(self):
        print('Eu sou um cachorro')

cachorro = Cachorro("Labrador")
cachorro2 = Cachorro("Pastor")
cachorro3 = Cachorro()

print(cachorro.raca)
print(cachorro3.raca)
