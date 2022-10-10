from string import *


def pruefziffer(Key):
    summe = 0
    i = 0
    for c in Key:
        ziffer = 0
        multiplikator = 0

        if str.isalpha(c):
            ziffer = ord(c) - 64 + 9
        else:
            ziffer = c

        if i % 3 == 0:
            multiplikator = 7
        elif i % 3 == 1:
            multiplikator = 3
        else:
            multiplikator = 1

        i = i+1
        summe = summe + int(ziffer) * multiplikator

    return summe % 10


if __name__ == "__main__":

    # ----------------------
    # NACH BELIEBEN ÄNDERBAR:
    Key_Ausweisnummer       = "LBBK3040F"   # Behördenziffer 'LBBK' und Ausweisnummer '3040F'
    Key_Geburtsdatum_invers = "880211"      # 11. Februar 1988
    Key_Ablaufdatum         = "261011"      # 11. Oktober 2026
    # ----------------------

    assert(len(Key_Ausweisnummer) == 9)
    assert(len(Key_Geburtsdatum_invers) == 6)
    assert(len(Key_Ablaufdatum) == 6)

    Ausweisnummer       = Key_Ausweisnummer + str(pruefziffer(Key_Ausweisnummer))
    Geburtsdatum_invers = Key_Geburtsdatum_invers + str(pruefziffer(Key_Geburtsdatum_invers))
    Ablaufdatum         = Key_Ablaufdatum + str(pruefziffer(Key_Ablaufdatum)) + "D"             # D = Deutschland
    Pruefziffer         = str(pruefziffer(Ausweisnummer+Geburtsdatum_invers+Ablaufdatum[:-1]))

    print("Ausweisfeld:      " + Ausweisnummer)
    print("Geburtstagfeld:   " + Geburtsdatum_invers)
    print("Ablaufdatum Feld: " + Ablaufdatum)
    print("Prüfziffer:       " + Pruefziffer + "\n")

    print("IDD<<"+Ausweisnummer+"<<<<<<<<<<<<<<<<<<<")
    print(Geburtsdatum_invers+"<"+Ablaufdatum+"<<<<<<<<<<<<<<<<<"+Pruefziffer)
    print("NACHNAME" + "<<" + "VORNAME" + "<" + "ZWEITNAME"+"<<<<<<<")
