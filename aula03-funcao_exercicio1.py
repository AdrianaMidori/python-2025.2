def verificar_par_impar(num):
    resto = num % 2
    if resto == 0:
        return 'O número é par'
    else:
        return 'O número é ímpar'
    

entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    numero = int(entrada)
    print(verificar_par_impar(numero))
else:
    print('Valor digitado não é um número inteiro')

    
