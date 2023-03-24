#!/usr/bin/env python3

import random
class Kostka:
  """
  Trida reprezentujici hraci kostku.
  """

  def __init__(self, pocetSten=6):
    self.__pocetSten = pocetSten

  def hod(self):
    return random.randint(1, self.__pocetSten)

  def __str__(self):
    return f"Kostka s {self.__pocetSten} stenami."

  def getPocetSten(self):
    return self.__pocetSten

  def setPocetSten(self, pocetSten):
    self.__pocetSten = pocetSten


if __name__=="__main__":
  k = Kostka(12)
  print(k)
  print(k.getPocetSten())
  k.setPocetSten(30)
  print(k.getPocetSten())
  print(k.hod())
  

