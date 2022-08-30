'''
Python Zumbi

Lista 2 - Exercício 01

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
