continua = True
while continua:
    nome = input('Informe o nome do aluno: ')
    nota1 = float(input('Informe a primeira nota do aluno: '))
    nota2 = float(input('Informe a segunda nota do aluno: '))
    media = (nota1+nota2)/2
    if media > 6.5:
        situacao = "aprovado"
    else:
        situacao = "reprovado"

    if (media >0) and (media <=10):
        print(f'A média foi {media}. O aluno está {situacao}.')
    else:
        print(f'Inconsistência nas notas informadas')  

    resp = input('Deseja continuar? (S/N) ')
    if resp.upper() == 'S':
        continua = True
    else:
        continua = False


 