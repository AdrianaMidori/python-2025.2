nome = input('Informe o nome do aluno: ')
nota1 = int(input('Informe a primeira nota do aluno: '))
nota2 = int(input('Informe a segunda nota do aluno: '))
media = (nota1+nota2)/2
if media >= 6.5:
    print(f'{nome} foi aprovado com a media {media}')
else:
    print(f'{nome} foi reprovado com a media {media}')

    
            