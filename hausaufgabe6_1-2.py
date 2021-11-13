# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:13:47 2020

"""

class Fahrzeug:
    #1. Erstellen Sie eine Klasse Fahrzeug, die die Attribute bezeichnung, 
    # neupreis, alter, und den Wertverlust pro Jahr wertverlust übergeben bekommt. 
    # wertverlust soll dabei als privates Attribut gespeichert werden. 
    # Berechnen Sie im Konstruktor außerdem den Restwert 
    # (Restwert = Neupreis - Alter in Jahren * Wertverlust pro Jahr) und 
    # speichern Sie ihn als Klassenattribut restwert ab. 
    # Das Erstellen eines Objekts könnte z.B. so aussehen:
    def __init__(self,bezeichnung,neupreis,alter,wertverlust):
        self.bezeichnung= bezeichnung
        self.neupreis=neupreis
        self.alter=alter
        self.set_Wertverlust(wertverlust) #loss of value, depreciasion
        self.restwert =self.neupreis - (self.alter * self.get_Wertverlust()) #residual value
    
    #2. Erstellen Sie eine Methode get_Wertverlust, die den Wertverlust des 
    # jeweiligen Fahrzeugs zurückgibt, und eine Methode set_Wertverlust, 
    # über die sich der Wertverlust setzen lässt. Achten Sie dabei darauf, 
    # dass in der Set Methode der Restwert des Fahrzeugs neu berechnet werden muss. 
    
    #@property
    def get_Wertverlust(self):
        return self._wertverlust
    
    #@get_Wertverlust.setter
    def set_Wertverlust(self,wertverlust):
        self._wertverlust=wertverlust
        
    Wertverlust=property(get_Wertverlust,set_Wertverlust)  
    
    #3. Überladen Sie den < Operator (__lt__), sodass der Restwert zweier 
    # verschiedener Fahrzeug-Objekte miteinander verglichen wird.
    def __lt__(self, other):
        in1=self.restwert
        in2=other.restwert
        if in1<in2:
           return "True"
        else:
           return "False"

if __name__ == "__main__":
    # 1.Erstellen eines Objekts vom Typ Fahrzeug
    VWGolf = Fahrzeug ("VW Golf", 25000.0, 5, 2500.0)
    print (VWGolf.restwert)
    
    # 2. Testen der Funktion get() set()
    print(VWGolf.get_Wertverlust())
    VWGolf.set_Wertverlust(3000.0)
    print(VWGolf.get_Wertverlust())
    print(VWGolf.restwert)
    
    # 3. Testen der Funktion lt()
    VWGolf = Fahrzeug("VW Golf", 25000.0, 5, 2500.0)
    Porsche911 = Fahrzeug("Porsche 911", 100000.0, 2, 10000.0)
    print(Porsche911 > VWGolf)
    print(Porsche911 < VWGolf)
        