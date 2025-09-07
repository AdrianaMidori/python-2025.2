from velha import Velha

jogo = Velha()

# Desenha o tabuleiro inicial
jogo.desenharTabuleiro()

while True:
    # Jogada do Humano
    entradaLinha = input('Digite a linha (0-2) ou "SAIR": ')
    if (entradaLinha.upper() == "SAIR"):
        break
    entradaColuna = input('Digite a coluna(0-2) ou "SAIR": ')
    if entradaColuna == "SAIR":
        break
    
    #Se alguma entrada não for número, pedir para fazer nova entrada
    if (not(entradaLinha.isdigit())) or (not(entradaColuna.isdigit)) or (entradaLinha=='') or (entradaColuna ==''):
        print('Entrada inválida')
        continue
    
    jogadaLinha = int(entradaLinha)
    jogadaColuna = int(entradaColuna)
    if (jogadaLinha > 2) or (jogadaColuna > 2):
        print('Entrada deve ser entre 0 e 2')
        continue
    
    #Se a posição desejada estiver vazia
    if jogo.tabuleiro[jogadaLinha][jogadaColuna] == ' ':
        jogo.receberJogada(jogadaLinha, jogadaColuna, 'X')
        jogo.desenharTabuleiro()
    else:
        print('Jogada inválida')
        continue

    #Verificar se houve vencedor
    temVencedor = jogo.verificarVencedor()
    if temVencedor:
        jogo.desenharTabuleiro()
        jogo.mostrarMsgVencedor()
        break

    # Jogada da Máquina
    temEspaco = jogo.verEspacoNoTabuleiro() 
    if temEspaco:  
        jogadaLinha = jogo.jogarMaquina()
        jogadaColuna = jogo.jogarMaquina()  

        #Caso seja sorteado uma posição já preenchida, continuar sorteando nova posição
        while (jogo.tabuleiro[jogadaLinha][jogadaColuna] != ' '):
            jogadaLinha = jogo.jogarMaquina()
            jogadaColuna = jogo.jogarMaquina()

        jogo.receberJogada(jogadaLinha, jogadaColuna, 'O')
        print("Máquina jogou")
        jogo.desenharTabuleiro()

    #Verificar se houve vencedor
    temVencedor = jogo.verificarVencedor()
    if temVencedor:
        jogo.desenharTabuleiro()
        jogo.mostrarMsgVencedor()
        break
    elif (not temEspaco):
        jogo.desenharTabuleiro()
        print('Não há mais opções de jogada. Jogo EMPATADO!')
        break
    
