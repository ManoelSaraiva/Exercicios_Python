'''
Python para Zumbis - Fernando Masanori

Lista 2 - Exercício 01

1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

'''

lado1 = int(input('Digite o primeiro lado do triangulo: '))
lado2 = int(input('Digite o segundo lado do triangulo: '))
lado3 = int(input('Digite o terceiro lado do triangulo: '))

if lado1 == lado2 and lado2 == lado3:
    print('Triangulo Equilátero')
elif lado1 == lado2 and lado3 != lado2:
    print('Triangulo Isosceles')
else:
    print('Triangulo Escaleno')
