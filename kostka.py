#!/usr/bin/env python3

import random
class Kostka:
  """
  Trida reprezentujici hraci kostku.
  """

  def __init__(self, pocetSten=6):
    self.pocetSten = pocetSten

  def hod(self):
    return random.randint(1, self.pocetSten)

  def __str__(self):
    return "Kostka s {0} stenami.".format(self.pocetSten)

if __name__=="__main__":
    k = Kostka()
    print(k.hod())
