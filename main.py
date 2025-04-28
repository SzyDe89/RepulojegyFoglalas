from legitarsasag import LegiTarsasag
from jarat import BelfoldiJarat, NemzetkoziJarat

def main():
    airline = LegiTarsasag("TurboTurbina")

    # Előre feltöltött járatok
    airline.jarat_hozzaadasa(BelfoldiJarat("B001", "Budapest", 15000))
    airline.jarat_hozzaadasa(BelfoldiJarat("B002", "Debrecen", 10000))
    airline.jarat_hozzaadasa(NemzetkoziJarat("N001", "Róma", 30000))
    airline.jarat_hozzaadasa(NemzetkoziJarat("N002", "London", 45000))
    airline.jarat_hozzaadasa(NemzetkoziJarat("N003", "Párizs", 40000))  
    airline.jarat_hozzaadasa(NemzetkoziJarat("N004", "Bécs", 20000))      

    # Előre feltöltött foglalások
    airline.jegy_foglalas("Foglal Elek", "B001")
    airline.jegy_foglalas("Utazó Béla", "N002")
    airline.jegy_foglalas("Késő Róbert", "N003")
    airline.jegy_foglalas("Repül Nóra", "B001")
    airline.jegy_foglalas("Száll István", "N002")
    airline.jegy_foglalas("Csúsz Ivett", "N004")
    airline.jegy_foglalas("Várakozó Gábor", "N001")
    airline.jegy_foglalas("Felszálló Dóra", "N003")
    airline.jegy_foglalas("Átszálló Tamás", "N004")   
    airline.jegy_foglalas("Viharos Károly", "B002") 

    while True:
        print("\nVálassz műveletet:")
        print("1 - Jegy foglalása")
        print("2 - Foglalás lemondása")
        print("3 - Foglalások listázása")
        print("4 - Kilépés")

        valasztas = input("Művelet száma: ")

        if valasztas == "1":
            airline.jaratok_listazasa()
            nev = input("Adja meg az ön nevét: ")
            jaratszam = input("Adja meg a foglalni kívánt járat számát: ")
            airline.jegy_foglalas(nev, jaratszam)
        elif valasztas == "2":
            nev = input("Adja meg az ön nevét: ")
            jaratszam = input("Adja meg a lemondani kívánt járat számát: ")
            airline.foglalas_lemondasa(nev, jaratszam)
        elif valasztas == "3":
            airline.foglalasok_listazasa()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
