'''

Python para Zumbis - Fernando Masanori

Lista 1 - Exercício 09

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

'''


km_percorridos = float(input('Qual a quilometragem percorrida ? '))

dias_de_aluguel = int(input('Digite a quantidade de dias de aluguel '))


print(
    f'A diária de aluguel foi {dias_de_aluguel * 60} e o valor dos km percorridos {km_percorridos * 0.15}')
