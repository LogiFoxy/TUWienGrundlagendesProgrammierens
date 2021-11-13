# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:50:35 2021

"""


def checkKuchen(Dict):
    nachbestellen = []
    for i in Dict:
         
         if "kuchen" in i and Dict[i] <5:
             nachbestellen.append(i)
         elif "kuchen" not in i:
            print(i, "ist kein Kuchen!")
         elif "kuchen" in i and Dict[i]>=5:
             print("Es gibt genug", i, "nämlich", Dict[i], "Stück")
    return nachbestellen

lager  =  {"obstkuchen":10,
           "marmorkuchen":4,
           "nusstorte":20, "kleinkuchen":33}
liste = checkKuchen(lager)

print("Nachbestellen:", liste)