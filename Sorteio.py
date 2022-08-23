"""
    Classe para realização de sorteio de jogos Lotofácil
"""
import random


class Sorteio:

    def __init__(self):
        self.__jogos = None
        self.__dezenas_lotofacil = None

    def gerar_jogos(self, qtd=1):
        self.__jogos = []
        for x in range(qtd):
            self.__dezenas_lotofacil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
            self.__jogos.insert(x, self.__sorteio_aleatorio(self.__dezenas_lotofacil))
        return self.__jogos

    def __sorteio_aleatorio(self, dezenas):
        self.__sorteio = []
        for x in range(15):
            self.__sorteio.append(dezenas.pop(random.randrange(0, len(dezenas))))
        self.__sorteio.sort()
        return self.__sorteio


if __name__ == "__main__":
    dezenas2 = Sorteio()
    print(dezenas2.gerar_jogos(5))
