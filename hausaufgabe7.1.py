# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:00:12 2020

"""
# Schreiben Sie basierend auf der Funktion Einlesen aus Hausaufgabe 5.1 
# eine Methode Einlesen_Check. Diese Methode soll das selbe machen wie die 
# Funktion Einlesen, aber zusätzlich überprüfen, ob die Information in der
# übergebenen Datei das richtige Format hat. Es sollen nur Fahrzeuge 
# gespeichert werden, für die Angaben im richtigen Format vorhanden sind.
def Einlesen_Check(filename):
    data_dict = {}
    #Fangen Sie dazu die folgenden typischen Fehler mit Hilfe von 
    #try-except-else Blöcken ab:
    try:
        with open(filename,'r') as fobj:
            for line in fobj:
                try:
                    data = line.split(',')
                    key  = data[0].strip()
                    neupreis    = float(data[1].strip())
                    alter       = float(data[2].strip())
                    wertverlust = float(data[3].strip())
                    data_dict[key] = [neupreis,alter,wertverlust]
                #2.Die Datei könnte anstatt Zahlenwerte für das Alter usw. 
                #etwas enthalten, das sich nicht zu einem Integer oder Float
                #konvertieren lässt.Siehe z.B. die Testdatei 
                #fahrzeuge_fehlerhaft_v1.txt auf TUWEL.
                except ValueError: 
                    print("Falscher Datentyp!")
                    pass
                #3.Die Datei könnte in einer Zeile falsche Trennzeichen, 
                #z.B. Strichpunkte (;) statt Beistrichen (,) enthalten bzw. 
                #eine falsche Anzahl an Angaben enthalten. Siehe z.B. die 
                #Testdatei fahrzeuge_fehlerhaft_v2.txt auf TUWEL. Geben Sie 
                #eine hilfreiche Fehlermeldung aus, wenn ein Fehler aufgetreten ist!
                except:
                    print("Falsche Trennzeichen oder falsche Anzahl von Werten!")
                    pass
            return data_dict
    #1.Die Datei könnte z.B. nicht existieren.
    except FileNotFoundError: 
        print("Datei 'fahrzeuge_existiertnicht.txt' nicht gefunden!")
      
if __name__ == "__main__":
    # Testen Sie Ihren Code mit einigen Beispielen. 
    # Wenn Ihre Funktion richtig funktioniert, sollten 
    # Sie in etwa folgende Ausgaben erhalten: Bei einer 
    # nicht existierenden Datei, z.B. fahrzeuge_existiertnicht.txt
    fahrzeugDict = Einlesen_Check("vehicles_existentnot.txt")
    print(fahrzeugDict)
    #Mit der Testdatei fahrzeuge_fehlerhaft_v1.txt
    fahrzeugDict = Einlesen_Check('fahrzeuge_fehlerhaft_v1.txt')
    print(fahrzeugDict)
    #Mit der Testdatei fahrzeuge_fehlerhaft_v2.txt:
    fahrzeugDict = Einlesen_Check('fahrzeuge_fehlerhaft_v2.txt')
    print(fahrzeugDict)