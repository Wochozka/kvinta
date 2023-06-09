#!/usr/bin/env python3

import kostka

class Bojovnik:
    """
    Trida reprezentujici bojovnika do areny.
    """
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        jmeno  - jmeno Bojovnika
        zivot  - zivot Bojovnika
        utok   - stala sila utoku Bojovnika
        obrana - stala sila obrany Bojovnika
        kostka - kostka pro upraveni sily utoku/obrany
        """
        
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
        self._zprava = ""

    def __str__(self):
        return f"Bojovnik jmenem {self.__jmeno}."
    
    @property
    def nazivu(self):
        return self.__zivot > 0
    
    def graficky_zivot(self):
        celkem = 15
        pocet = int(self.__zivot / self.__max_zivot * celkem)
        return f"[{'#'*pocet}{' '*(celkem-pocet)}]"
    
    def utok(self, souper):
        uder = self.__utok + self.__kostka.hod()
        souper.obrana(uder)
    
    def obrana(self, uder):
        zraneni = uder - (self.__obrana + self.__kostka.hod())
        zprava = f"{self.__jmeno} utrpel zranei o sile {zraneni}."
        if zraneni > 0:
            self.__zivot = self.__zivot - zraneni
            if self.__zivot <= 0:
                self.__zivot = 0
                zprava = zprava[:-1] + " a zemrel."
        else:
            zprava = f"{self.__jmeno} zcela odrazil utok."
        self.setZprava(zprava)
    
    def getZprava(self):
        return self._zprava
    
    def setZprava(self, zprava):
        self._zprava = zprava


if __name__=="__main__":
    k = kostka.Kostka(10)
    a = Bojovnik("Zlatka", 70, 10, 8, k)
    b = Bojovnik("Terka", 60, 15, 9, k)

    while a.nazivu and b.nazivu:
        a.utok(b)
        print(a, a.getZprava())
        print(a.graficky_zivot())
        b.utok(a)
        print(b, b.getZprava())
        print(b.graficky_zivot())
        x = input()
    print(a, a.getZprava())
    print(b, b.getZprava())

        


