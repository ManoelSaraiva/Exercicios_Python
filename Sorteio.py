'''
    Classe para realização de sorteio de jogos Lotofácil

'''
import random


class Sorteio():

    def __init__(self):
        pass

    def gerar_jogos(self, qtd=1):
        self.dezenas_lotofacil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                  12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.jogos = []
        for x in range(qtd):
            self.jogos.append(self.__sorteio_aleatorio(self.dezenas_lotofacil))
        return self.jogos

    def __sorteio_aleatorio(self, dezenas):
        self.sorteio = []
        for x in range(15):
            self.sorteio.append(dezenas.pop(random.randrange(0, len(dezenas))))
        self.sorteio.sort()
        return self.sorteio


dezenas2 = Sorteio()


# print(dezenas2.sorteio_aleatorio(dezenas_lot))
print(dezenas2.gerar_jogos())
