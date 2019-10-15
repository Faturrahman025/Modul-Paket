import math


#Energi Potensial
def EnergiPotensial(m, g, h):
    return m * g * h

#Energi Kinetik
def EnergiKinetik(m, v):
    return 1/2 * m * v * v

#Energi Mekanik
def EnergiMekanik(ep, ek):
    return ep + ek
