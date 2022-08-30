'''
Python Zumbi

Lista 2 - Exercício 03

'''

peixe_pescado = int(input('Digite a quantos quilos de peixe foram pescados: '))
excesso_peixe = 0
multa = 0

if peixe_pescado > 50:
    excesso_peixe = peixe_pescado - 50
    multa = excesso_peixe * 4
    print(
        f'Voce excedeu a quantidade de peixes em {excesso_peixe} quilos e terá que pagar R$ {multa} de multa')
else:
    print(
        f'Continue pescando o excesso esta me {excesso_peixe} e a multa ainda é R$ {multa}')
