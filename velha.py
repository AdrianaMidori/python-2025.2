import random

class Velha():
    def __init__(self):
        self.tabuleiro = [[' ', ' ', ' '] ,[' ', ' ', ' '] , [' ', ' ', ' ']]


    def desenharTabuleiro(self):
        print(' ' + self.tabuleiro[0][0] + ' | ' + self.tabuleiro[0][1] + ' | ' + self.tabuleiro[0][2])
        print('-----------')
        print(' ' + self.tabuleiro[1][0] + ' | ' + self.tabuleiro[1][1] + ' | ' + self.tabuleiro[1][2])
        print('-----------') 
        print(' ' + self.tabuleiro[2][0] + ' | ' + self.tabuleiro[2][1] + ' | ' + self.tabuleiro[2][2])

    def receberJogada(self, linha, coluna):
        if self.linha == 0:
            self.tabuleiro[0].insert(coluna, 'X')
        elif self.linha == 1:
            self.tabuleiro[1].insert(coluna, 'X')
        elif self.linha == 2:
            self.tabuleiro[2].insert(coluna, 'X')

    def jogarMaquina(self):
        return random.randint(0, 2)  
        













   