from velha import Velha

jogo = Velha()

# Desenha o tabuleiro inicial
jogo.desenharTabuleiro()

# Jogada do Humano
jogadaLinha = int(input('Digite a posição da linha: '))
jogadaColuna = int(input('Digite a posição da coluna: '))
jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'X'
jogo.desenharTabuleiro()

# Jogada da Máquina
jogadaLinha = jogo.jogarMaquina()
jogadaColuna = jogo.jogarMaquina()
jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'O'
print("Maquina jogou")
jogo.desenharTabuleiro()

