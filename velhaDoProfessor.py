import random

class Velha():
    def __init__(self):
        self.ganhador = False
        self.tabuleiro = [[' ', ' ', ' '] ,[' ', ' ', ' '] , [' ', ' ', ' ']]

    def desenharTabuleiro(self):
        print(' ' + self.tabuleiro[0][0] + ' | ' + self.tabuleiro[0][1] + ' | ' + self.tabuleiro[0][2])
        print('-----------')
        print(' ' + self.tabuleiro[1][0] + ' | ' + self.tabuleiro[1][1] + ' | ' + self.tabuleiro[1][2])
        print('-----------') 
        print(' ' + self.tabuleiro[2][0] + ' | ' + self.tabuleiro[2][1] + ' | ' + self.tabuleiro[2][2])

    def jogarMaquina(self):
        return random.randint(0, 2)  
    
    def verificarVencedor(self):
        dicVencedor = {}

        for i in ['X', 'O']:
            #horizontal
            dicVencedor[i] = (self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == i)
            dicVencedor[i] = (self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == i) or dicVencedor[i]
            dicVencedor[i] = (self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2] == i) or dicVencedor[i]
        
            #vertical
            dicVencedor[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == i) or dicVencedor[i]
            dicVencedor[i] = (self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == i) or dicVencedor[i]
            dicVencedor[i] = (self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2] == i) or dicVencedor[i]

            #diagonal
            dicVencedor[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == i) or dicVencedor[i]
            dicVencedor[i] = (self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == i) or dicVencedor[i]

        if dicVencedor['X'] or dicVencedor['O']:
            self.ganhador = True

        return dicVencedor
    
    def verificarEspaco(self):
        espaco = False
        for x in range(3):
            for y in range(3):
                if self.tabuleiro[x][y] == ' ':
                    espaco = True
                    return espaco
                
        return espaco
