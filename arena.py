#!/usr/bin/env python3

import kostka
import bojovnik

class Arena():

    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.__bojovnik1 = bojovnik1
        self.__bojovnik2 = bojovnik2
        self._kostka = kostka
    
    def zapas(self):
        while self.__bojovnik1.nazivu and self.__bojovnik2.nazivu:
            self.__bojovnik1.utok(self.__bojovnik2)
            print(self.__bojovnik1.getZprava())
            self.__bojovnik2.utok(self.__bojovnik1)
            print(self.__bojovnik2.getZprava())

if __name__=="__main__":
    k1 = kostka.Kostka()
    b1 = bojovnik.Bojovnik("Adam", 100, 40, 30, k1)
    b2 = bojovnik.Bojovnik("Karel", 120, 35, 33, k1)

    a = Arena(b1, b2, k1)
    a.zapas()

        


