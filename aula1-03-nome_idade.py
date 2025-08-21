nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))

#usando interpolação
print(f'{nome} tem {idade}  anos' )

#usando concatenação
print(nome + " tem " + str(idade) + " anos")