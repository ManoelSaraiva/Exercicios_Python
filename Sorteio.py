'''
    Classe para realização de sorteio de jogos Lotofácil

'''
import random


class Sorteio():

    def __init__(self):
        pass

    def sorteio_aleatorio(self):
        self.__dezenas_lotofacil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.sorteio = []
        for x in range(15):
            self.sorteio.append(self.__dezenas_lotofacil.pop(
                random.randrange(0, len(self.__dezenas_lotofacil))))
        self.sorteio.sort()
        return self.sorteio


dezenas2 = Sorteio()

print(dezenas2.sorteio_aleatorio())


