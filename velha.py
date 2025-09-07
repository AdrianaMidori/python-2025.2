import random

class Velha():
    def __init__(self):
        self.tabuleiro = [[' ', ' ', ' '] ,[' ', ' ', ' '] , [' ', ' ', ' ']]
        self.vencedor = ''

    def desenharTabuleiro(self):
        print(' ' + self.tabuleiro[0][0] + ' | ' + self.tabuleiro[0][1] + ' | ' + self.tabuleiro[0][2])
        print('-----------')
        print(' ' + self.tabuleiro[1][0] + ' | ' + self.tabuleiro[1][1] + ' | ' + self.tabuleiro[1][2])
        print('-----------') 
        print(' ' + self.tabuleiro[2][0] + ' | ' + self.tabuleiro[2][1] + ' | ' + self.tabuleiro[2][2])

    def receberJogada(self, linha, coluna, valor):
        self.linha = linha
        self.coluna = coluna
        self.valor = valor
        self.tabuleiro[linha][coluna] = self.valor           

    def jogarMaquina(self):
        return random.randint(0, 2)  
        

    def verEspacoNoTabuleiro(self):
        temEspaco = False
        for itemLinha in self.tabuleiro:
            for itemColuna in itemLinha:
                if itemColuna == ' ':
                    temEspaco = True
        return temEspaco        
        
    def verVencedorNasLinhas(self):
        lista = []
        for itemLinha in self.tabuleiro:
            for itemColuna in itemLinha:
                lista.append(itemColuna)

            #Se os elementos da lista são iguais, houve vencedor
            if (lista[0] != ' ') and (lista[0] == lista[1]) and (lista[0] == lista[2]):
                self.vencedor = lista[0]
                return True
            lista =[]

        return False

    def verVencedorNasColunas(self):
        lista =[]
        for coluna in range(3):
            for linha in range(3):
                lista.append(self.tabuleiro[linha][coluna])
                
            if (lista[0] != ' ') and (lista[0] == lista[1]) and (lista[0] == lista[2]):
                self.vencedor = lista[0]
                return True
            lista = [] 
        return False  

    def verVencedorNasDiagonais(self):
        if (self.tabuleiro[0][0] != ' ') and \
            (self.tabuleiro[0][0]==self.tabuleiro[1][1]) and \
            (self.tabuleiro[0][0]== self.tabuleiro[2][2]):

            self.vencedor = self.tabuleiro[0][0]
            return True
        
        if (self.tabuleiro[0][2] != ' ') and \
            (self.tabuleiro[0][2]==self.tabuleiro[1][1]) and \
            (self.tabuleiro[0][2]== self.tabuleiro[2][0]):
            
            self.vencedor = self.tabuleiro[0][2]
            return True
        
        return False

    def verificarVencedor(self):
        temVencedorLinha = self.verVencedorNasLinhas()
        temVencedorColuna = self.verVencedorNasColunas()
        temVencedorDiagonal = self.verVencedorNasDiagonais()
        if temVencedorLinha or temVencedorColuna or temVencedorDiagonal:
            return True

    def mostrarMsgVencedor(self):
        if self.vencedor == 'X':
            print('PARABÉNS! VOCÊ VENCEU!')  
        elif self.vencedor == 'O':
            print('FIM DE JOGO! A máquina venceu!')   






   

    









   