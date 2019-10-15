import Fatur.RumusFisika

def main():
    #Energi Kinetik
    m = 2
    v = 10
    

    ek = Fatur.RumusFisika.EnergiKinetik(m, v)
    print("ENERGI KINETIK")
    print("Massa\t\t: ", m)
    print("Kecepatan\t: ", v)
    print("Energi Kinetik\t: ", ek)

if __name__ == "__main__":
    main()
