'''

Python para Zumbis - Fernando Masanori

Lista 1 - Exercício 04

Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.

'''

salario_base = float(input('Digite o valor do salario: '))
porcentagem_aumento = float(input('Digite a porcentagem de aumento: '))

novo_salario = salario_base + (salario_base * (porcentagem_aumento / 100))

print(f'O novo salario é {novo_salario}')
