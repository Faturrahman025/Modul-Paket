import Fatur.RumusFisika

def main():
    #Energi Potensial
    m = 2
    g = 4
    h = 5

    ep = Fatur.RumusFisika.EnergiPotensial(m, g, h)
    print("ENERGI POTENSIAL")
    print("Massa\t\t\t: ", m)
    print("Percepatan gravitasi\t: ", g)
    print("Tinggi\t\t\t: ", h)
    print("Energi Potensial\t: ", ep)
    

    #Energi Kinetik
    m = 2
    v = 10
    
    ek = Fatur.RumusFisika.EnergiKinetik(m, v)
    print("\nENERGI KINETIK")
    print("Massa\t\t: ", m)
    print("Kecepatan\t: ", v)
    print("Energi Kinetik\t: ", ek)


    #Energi Mekanik
    ep = 25
    ek = 26
    

    em = Fatur.RumusFisika.EnergiMekanik(ep, ek)
    print("\nENERGI MEKANIK")
    print("Energi Potensial\t: ", ep)
    print("Energi Kinetik\t\t: ", ek)
    print("Energi Mekanik\t\t: ", em)

if __name__ == "__main__":
    main()
