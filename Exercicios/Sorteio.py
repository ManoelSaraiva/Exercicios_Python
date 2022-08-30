"""
Classe para realização de sorteio de jogos Lotofácil.
"""
import random


class Sorteio:
    def __init__(self):
        self.__jogos = None
        self.DENZENAS_LOTOFACIL = None

    def gerar_jogos(self, qtd_jogos=1):
        self.__jogos = []
        for jogo in range(qtd_jogos):
            self.__DENZENAS_LOTOFACIL = [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
            ]
            self.__jogos.insert(
                jogo, self.__sorteio_aleatorio(self.__DENZENAS_LOTOFACIL)
            )
        return self.__jogos

    def __sorteio_aleatorio(self, dezenas: list) -> list:
        self.__sorteio = []
        for _ in range(15):
            self.__sorteio.append(
                dezenas.pop(random.randrange(0, len(dezenas)))
            )
        self.__sorteio.sort()
        return self.__sorteio


if __name__ == '__main__':
    dezenas2 = Sorteio()

    print(dezenas2.gerar_jogos())
    print(type(dezenas2.gerar_jogos()))
