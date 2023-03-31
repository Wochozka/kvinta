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

    def __str__(self):
        return f"Bojovnik jmenem {self.__jmeno}."
    
    @property
    def nazivu(self):
        return self.__zivot > 0
    
    def graficky_zivot(self):
        celkem = 15
        pocet = int(self.__zivot / self.__max_zivot * celkem)
        return f"[{'#'*pocet}{' '*(celkem-pocet)}]"


if __name__=="__main__":
    k = kostka.Kostka(10)
    b = Bojovnik("Zlatka", 5, 10, 8, k)
    print(b)
    print(b.nazivu)
    print(b.graficky_zivot())
    print(k.hod())
  

