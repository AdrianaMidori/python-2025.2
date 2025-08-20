continua = True
while continua:
    nome = input('Informe o nome do(a) aluno(a): ')
    nota1 = int(input('Informe a primeira nota do(a) aluno(a): '))
    nota2 = int(input('Informe a segunda nota do(a) aluno(a): '))
    media = (nota1+nota2)/2
    if media >= 6.5:
        print(f'{nome} foi aprovado(a) com a média {media}')
    else:
        print(f'{nome} foi reprovado(a) com a média {media}')

    resp = input('Deseja continuar? (S/N) ')
    if resp.upper() == 'S':
        continua = True
    else:
        continua = False