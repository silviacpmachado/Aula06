# calcula media - 1 Aluno
# for n in range(10): quando for testar, coloque um numero menor. ao invés de pedir 10 alunos, faça com 3. Se der certo, mude para 10.
#     n1 = float(input('Nota 1:'))
#     n2 = float(input('Nota 2:'))
#     n3 = float(input('Nota 3:'))
#     n4 = float(input('Nota 4:'))
#     media = (n1 + n2 + n3 + n4) / 4
#     print(media)

for aluno in range(3):
    print(f'\nAluno {aluno + 1}')
    n1 = float(input('Informe a nota1: '))
    n2 = float(input('Informe a nota2: '))
    n3 = float(input('Informe a nota3: '))
    n4 = float(input('Informe a nota4: '))

    media = (n1 + n2 + n3 + n4) / 4
    print (f'A média é {media}')
