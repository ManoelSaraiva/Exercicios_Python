'''
Python Zumbi

Lista 2 - Exercício 02

'''

ano = int(input('Digite um ano ex: 1996 : '))

if (ano % 4) == 0 or (ano % 100) == 0 or (ano % 400) == 0:
    print(f' {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
