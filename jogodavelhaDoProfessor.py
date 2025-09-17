from velhaDoProfessor import Velha

def mostrarResultado(resultado):
    if resultado ['X']:
        print('X venceu!')

    if resultado ['O']:
        print('O venceu!')

    if not jogo.verificarEspaco():
        print('Jogo empatou!')

jogo = Velha()

# Desenha o tabuleiro inicial
jogo.desenharTabuleiro()

while jogo.verificarEspaco():
    while True:
        # Jogada do humano
        jogadaLinha = int(input('Digite a linha: '))
        jogadaColuna = int(input('Digite a coluna: '))

        if jogo.tabuleiro[jogadaLinha][jogadaColuna] == ' ':
            jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'X'
            break

    #Verificação do vencedor
    resultado = jogo.verificarVencedor()
    jogo.desenharTabuleiro()
    mostrarResultado(resultado)
    if jogo.ganhador:
        break
    
    while True:
        # Jogada da máquina
        jogadaLinha = jogo.jogarMaquina()
        jogadaColuna = jogo.jogarMaquina()

        if jogo.tabuleiro[jogadaLinha][jogadaColuna] == ' ':    
            jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'O'
            print('Máquina jogou')
            break

    #Verificação do vencedor
    resultado = jogo.verificarVencedor()
    jogo.desenharTabuleiro()
    mostrarResultado(resultado)
    if jogo.ganhador:
        break

    jogo.desenharTabuleiro()



