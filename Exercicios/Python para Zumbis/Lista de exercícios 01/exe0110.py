'''

Python para Zumbis - Fernando Masanori

Lista 1 - Exercício 10

Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.

'''


cigarros_por_dia = int(
    input('Qual a quantidade de cigarros fumados por dia ? '))

anos_fumando = int(input('Quantos anos você fuma ? '))

cigarros_consumidos = (anos_fumando * 365) * cigarros_por_dia

quantidade_dias = ((cigarros_consumidos * 10) / 60) / 24


print(f'O total de perda foi {quantidade_dias} dia')
