from jarat import Jarat
from jegyfoglalas import JegyFoglalas

class LegiTarsasag:
    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadasa(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        for jarat in self.jaratok:
            print(f"{jarat.jaratszam} - {jarat.celallomas} ({jarat.jarat_tipus()}) - {jarat.jegyar} Ft")

    def jegy_foglalas(self, utas_nev: str, jaratszam: str):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                foglalas = JegyFoglalas(utas_nev, jarat)
                self.foglalasok.append(foglalas)
                print(f"Sikeres foglalás {utas_nev} részére, ár: {jarat.jegyar} Ft")
                return
        print("Nincs ilyen járat!")

    def foglalas_lemondasa(self, utas_nev: str, jaratszam: str):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                print("A foglalás sikeresen le lett mondva.")
                return
        print("Nincs ilyen foglalás.")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        for foglalas in self.foglalasok:
            print(f"{foglalas.utas_nev} - {foglalas.jarat.jaratszam} ({foglalas.jarat.celallomas})")
