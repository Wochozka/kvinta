#!/usr/bin/env python3

import kostka
import bojovnik

class Arena():

    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.__bojovnik1 = bojovnik1
        self.__bojovnik2 = bojovnik2
        self._kostka = kostka
    
    def zapas(self):
        import random as _random
        
        if _random.randint(0,1):
            (self.__bojovnik1, self.__bojovnik2) = (self.__bojovnik2, self.__bojovnik1)
        
        while self.__bojovnik1.nazivu and self.__bojovnik2.nazivu:
            self.__bojovnik1.utok(self.__bojovnik2)
            self.vykresli()
            self.vypis_zpravu(self.__bojovnik1.getZprava())
            self.vypis_zpravu(self.__bojovnik2.getZprava())
            if self.__bojovnik2.nazivu:
                self.__bojovnik2.utok(self.__bojovnik1)
                self.vykresli()
                self.vypis_zpravu(self.__bojovnik2.getZprava())
                self.vypis_zpravu(self.__bojovnik1.getZprava())

    
    def vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess

        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call("clear")

    def vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(1)

    def vykresli_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f"Zivot: {bojovnik.graficky_zivot()}")
    
    def vykresli(self):
        self.vycisti_obrazovku()
        print("---------------- Arena --------------------\n")
        self.vykresli_bojovnika(self.__bojovnik1)
        print()
        self.vykresli_bojovnika(self.__bojovnik2)


if __name__=="__main__":
    k1 = kostka.Kostka()
    b1 = bojovnik.Bojovnik("Adam", 100, 50, 30, k1)
    b2 = bojovnik.Bojovnik("Karel", 120, 35, 33, k1)

    a = Arena(b1, b2, k1)
    a.zapas()

        


