nome = input('Informe o nome: ')
idade =int(input('Informe a idade :'))

genero = input('Informe o gênero (1-Masculino/2-Feminino) : ')
if genero == '1':
    genero = 'M'
elif genero == '2':
    genero = 'F'

if idade > 50:
    print(f'{nome} tem {idade} anos e é experiente. {genero}')
else:
    print(f'{nome} tem {idade} anos, está em treinamento. {genero}')
    