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

if __name__ == "__main__":
    main()
