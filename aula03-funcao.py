# Função que não recebe parâmetros e não retorna valor
def exibirMensagem():
    print('Olá, eu sou o Python')

exibirMensagem()

# Função que recebe parâmetro e não retorna valor
def exibirMensagemPlus(mensagem):
    print('Olá, eu sou o Python ' + mensagem)

exibirMensagemPlus("José")

# Função que recebe parâmetro e retorna valor
def multiplicar(numero1, numero2):
    valor = numero1 * numero2
    return valor

print(multiplicar(4, 2))

# Função que não recebe parâmetro e retorna valor
def acenderFarol():
    return "Farol aceso"

print(acenderFarol())