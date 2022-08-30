'''

Python para Zumbis - Fernando Masanori

Lista 1 - Exercício 05

Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar

'''

preço_mercadoria = float(input('Qual o preço da mercadoria: '))
percentual_desconto = float(input('Qual o percentual de desconto: '))

preço_a_pagar = preço_mercadoria - \
    (preço_mercadoria * (percentual_desconto / 100))

print(f'O preço a pagar é de {preço_a_pagar}')
