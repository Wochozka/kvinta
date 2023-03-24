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
    return f"Kostka s {self.pocetSten} stenami."

if __name__=="__main__":
    k = Kostka(12)
    print(k)
    print(k.hod())
