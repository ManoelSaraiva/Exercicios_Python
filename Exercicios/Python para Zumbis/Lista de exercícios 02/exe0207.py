'''

Python para Zumbis - Fernando Masanori

Lista 2 - Exercício 07

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

'''


metros_a_pintar = float(input('Digite a area a ser pintada: '))

litros_de_tinta = metros_a_pintar / 3

latas_de_tinta = litros_de_tinta / 18


# Preciso arrumar aqui
if latas_de_tinta % 1 != 0:
    print(f'Comprar {int(latas_de_tinta) + 1} de tinta')
else:
    print(f'Comprar {int(latas_de_tinta)} lata de tinta')
