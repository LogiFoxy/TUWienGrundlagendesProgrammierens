# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:23:02 2020
"""
# Verwenden Sie das Modul doctest, um Ihre Klasse Fahrzeug aus Hausaufgabe 6.1 zu testen:
# 1.Kopieren Sie hierfür die Lösung von Hausaufgabe 6.1 aus TUWEL in ein neues Python-File.
# 2.Schreiben Sie für alle Methoden der Klasse (also Konstruktor, set_Wertverlust, 
# get_Wertverlust, und < Operator) jeweils einen Test. Das Testen von privaten Attributen 
# des Konstruktors ist nicht so einfach - beschränken Sie sich beim Testen des Konstruktors 
# daher auf die restlichen Attribute (bezeichnung, neupreis, alter, restwert). 
# Vergessen Sie nicht darauf bei der Methode set_Wertverlust zu testen, ob auch das 
# Attribut restwert korrekt neu berechnet wird.
class Fahrzeug:
    def __init__(self,bezeichnung,neupreis,alter,wertverlust):

        """
        >>> Auto= Fahrzeug('VW Golf', 25000.0, 5, 2500.0)
        >>> Auto.bezeichnung
        'VW Golf'
        >>> print(Auto.neupreis)
        25000.0
        >>> print(Auto.alter)
        5
        >>> print(Auto.restwert)
        12500.0
        """
        
        _="""
        >>> print(Auto.__wertverlust)
        2500.0
        """

        self.bezeichnung = bezeichnung
        self.neupreis = neupreis
        self.alter = alter
        self.__wertverlust = wertverlust
        self.restwert = neupreis - alter * wertverlust

        def get_Wertverlust(self):

            """ 
            >>> print(Auto.get_Wertverlust())
            2500.0
            """
            return self.__wertverlust    

        def set_Wertverlust(self,wertverlust_neu):

            """ 
            >>> print(Auto.set_Wertverlust())
            3000.0
            >>> print(Auto.restwert())
            10000.0
            """
            self.__wertverlust = wertverlust_neu
            self.restwert = self.neupreis - self.alter * wertverlust_neu 

        def __lt__(self,other):

            """
            >>> print(Auto.restwert<Auto.restwert)
            True
            """
            return self.restwert < other.restwert
#3.Führen Sie danach den doctest im Hauptteil des Skripts aus.
if __name__ == "__main__":
    import doctest 
    doctest.testmod(verbose=True)