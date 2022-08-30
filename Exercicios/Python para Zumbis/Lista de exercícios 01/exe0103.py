'''

Python para Zumbis - Fernando Masanori

Lista 1 - Exercício 03

Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos

'''

qtd_dias = int(input('Digite a quantidade de dias: '))  # 86400 segundos
qtd_horas = int(input('Digite a quantidade de horas: '))  # 3600 segundos
qtd_minutos = int(input('Digite a quantidade de minutos: '))  # 60 segundos
qtd_segundos = int(input('Digite a quantidade de segundos : '))  # 1 segundo

segundos_totais = (qtd_dias * 86400) + (qtd_horas * 3600) + \
    (qtd_minutos * 60) + (qtd_segundos)

print(f'O valor convertido para segundos é igual a {segundos_totais} segundos')
