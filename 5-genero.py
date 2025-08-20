nome = input('Informe o nome: ')
idade = int(input('Informe a idade :'))
genero = input('Infome o gênero (Masculino/Feminino) : ')
genero_upper = genero.upper()
if genero_upper == 'MASCULINO':
    genero = 'M'
elif genero_upper == 'FEMININO':
    genero = 'F'
else:
    print('Genero incorreto')


if idade > 50:
    print(f' {nome} tem {idade} e é experiente. {genero}')
else:
    print(f' {nome} tem {idade} anos, está em treinamento. {genero}')
    