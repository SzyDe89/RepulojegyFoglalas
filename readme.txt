# Repülőjegy Foglalási Rendszer ✈️ - Turbó Turbina Airlines

Ez a projekt egy egyszerű repülőjegy foglalási rendszert valósít meg Python nyelven, objektumorientált programozási elvek felhasználásával. A rendszer lehetővé teszi járatokra jegyek foglalását, foglalások lemondását és az aktuális foglalások listázását.

## 📚 Projekt felépítése

- **jarat.py** – Járat (absztrakt osztály), BelföldiJarat, NemzetkoziJarat
- **jegyfoglalas.py** – JegyFoglalas osztály
- **legitarsasag.py** – LegiTarsasag osztály, amely kezeli a járatokat és foglalásokat
- **main.py** – A program indító fájlja
- **adatok.txt** – Név, szak, Neptun-kód

## 🛠️ Funkciók

- Járatok listázása
- Jegy foglalása
- Foglalás lemondása
- Foglalások listázása

## 🛫 Előre feltöltött adatok

- **Légitársaság neve:** Turbó Turbina
- **Járatok:**
  - B001 - Budapest (Belföldi) - 15 000 Ft
  - B002 - Debrecen (Belföldi) - 10 000 Ft
  - N001 - Róma (Nemzetközi) - 30 000 Ft
  - N002 - London (Nemzetközi) - 45 000 Ft
  - N003 - Párizs (Nemzetközi) - 40 000 Ft
  - N004 - Bécs (Nemzetközi) - 20 000 Ft  

- **Foglalók példanevei:**
  - Foglal Elek
  - Utazó Béla
  - Késő Róbert
  - Repül Nóra
  - Száll István
  - Csúsz Ivett
  - Várakozó Gábor
  - Felszálló Dóra
  - Átszálló Tamás
  - Viharos Károly

## 🧪 Használat

1. Klónozd a repository-t.
2. Nyisd meg PyCharm-ban vagy más IDE-ben.
3. Futtasd a `main.py` fájlt.
