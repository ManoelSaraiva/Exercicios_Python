'''

Python para Zumbis - Fernando Masanori

Lista 2 - Exercício 06

Faça um Programa que pergunte quanto você ganha por hora e o número 
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário
bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. 
Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo:

a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$

'''


salario_hora = float(input('Qual o valor do salario hora ? '))
horas_trabalhando = int(
    input('Qual a quantidade de horas trabalhadas no mês: '))

salario_bruto = salario_hora * horas_trabalhando
valor_ir = salario_bruto * (11 / 100)
valor_inss = salario_bruto * (8 / 100)
valor_sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - (valor_ir + valor_inss + valor_sindicato)

print('')
print(f'Salario bruto = {salario_bruto}')
print(f'IR = {valor_ir}')
print(f'INSS =  {valor_inss}')
print(f'Sindicato = {valor_sindicato}')
print(f'Salario liquido = {salario_liquido}')
