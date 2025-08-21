nome = input('Informe o nome: ')
idade =int(input('Informe a idade :'))
sexo = input('Digite o gênero - Masculino ou Feminino ')

'''
genero = input('Informe o gênero (1-Masculino/2-Feminino) : ')
if genero == '1':
    genero = 'M'
elif genero == '2':
    genero = 'F'
'''
if (sexo.upper() == "MASCULINO"):
    sexo = "M"
elif (sexo.upper() == "FEMININO"):
    sexo = "F"
else:
    sexo = "Gênero não esperado"


if idade > 50:
    print(f'{nome} tem {idade} anos e é experiente. ({sexo})')
else:
    print(f'{nome} tem {idade} anos, está em treinamento. ({sexo})')


    