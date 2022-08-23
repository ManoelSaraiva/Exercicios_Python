'''
    Classe para realização de sorteio de jogos Lotofácil

'''


class Sorteio():

    #self.dezenas_lotofacil = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    def __init__(self):
        self.dezenas_lotofacil = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        

    def sorteio_aleatorio(self):
        for dezena in self.dezenas_lotofacil:
            print(dezena)


dezenas2 = Sorteio()

dezenas2.sorteio_aleatorio()
