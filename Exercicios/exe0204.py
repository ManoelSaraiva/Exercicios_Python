'''
Python Zumbi

Lista 2 - Exercício 04

'''

numero_01 = int(input('Digite o primeiro numero: '))
numero_02 = int(input('Digite o segundo numero: '))
numero_03 = int(input('Digite o terceiro numero: '))

print(f'\nNumero A: {numero_01} , Numero B: {numero_02} e Numero C: {numero_03} \n')

if numero_01 > numero_02 and numero_01 > numero_03:
    print(f'O numero A {numero_01} é o maior')
elif numero_02 > numero_03:
    print(f'O numero B {numero_02} é o maior')
else:
    print(f'O numero C {numero_03} é o maior')
