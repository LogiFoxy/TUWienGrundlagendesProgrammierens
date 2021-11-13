# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:31:12 2021

"""

class Messung:
    def __init__(self, Messreihe, Messwerte):
        self.Messreihe = Messreihe
        self.__Messwerte = Messwerte
    def __str__(self):
        return f"Name der Messreihe: {self.Messreihe}, Messwerte: {self.__Messwerte}"
    def Mittelwert(self):
        mittelwert = 0
        for i in self.__Messwerte:
            mittelwert += i
        mittelwert = mittelwert/len(self.__Messwerte)
        return mittelwert
    def __lt__(self, Ziel):
        Kleiner = False
        if self.Mittelwert() < Ziel.Mittelwert():
            Kleiner = True
            return f"Mittelwert kleiner: {Kleiner}"
        else:
            return f"Mittelwert kleiner: {Kleiner}"


M1 = Messung("Hasen", [1.3, 2.6, 3.3])
M2 = Messung("Katzen", [3.2, 3.4, 1.2])
print(M1)
print(M1.Mittelwert())
print(M2)
print(M2.Mittelwert())
print(M2 < M1, M1 < M2)