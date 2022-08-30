'''
Python para Zumbis - Fernando Masanori

Lista 2 - Exercício 03

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. 
Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

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
