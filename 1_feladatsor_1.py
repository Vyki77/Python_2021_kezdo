# Kiíratás, adatbekérés billentyűzetről, változók, matematikai műveletek

# 1. feladat
# Programunk kérje be egy ember lakhelyének irányítószámát, a várost, a közterület nevét, a közterület jellegét,
# a házszámot és végül írja ki egy sorban a következő formátumban: Pl.: 1042 Budapest Tanoda tér 2. (lakcim)

# irszam = input('Kérem adja meg írányító számát: ')
# varos = input('Kérem adja meg a város nevét: ')
# kozter = input('Kérem adja meg a közterület nevét : ')
# kozterjellege = input('Kérem adja meg közterület jellegét: ')
# hazszam = input('Kérem adja meg a házszámot: ')
# print(f'{irszam} {varos} {kozter} {kozterjellege} {hazszam}.' )

# 2. feladat
# Olvassunk be két vezeték- és két keresztnevet, és írassuk ki az ezekből képezhető neveket! (nevek)

# vnev1 = input('Kérem adja meg az első vezetéknevet: ')
# vnev2 = input('Kérem adja meg a második vezetéknevet: ')
# knev1 = input('Kérem adja meg az első keresztnevet: ')
# knev2 = input('Kérem adja meg a második keresztnevet: ')
#
# print(f'{vnev1} {knev1}\n{vnev1} {knev2}\n{vnev2} {knev1}\n{vnev2} {knev2}')

# 3. feladat
# Olvassuk be a havi fizetést, és eredményként írassuk ki az éves fizetést!
# Milyen típusú változókat használhatunk? (fizetes)

# havi_ber = int(input('Kérem adja meg a havi bérét (Ft): '))
# eves_ber = havi_ber * 12
# print(f'Az éves fizetése: {eves_ber} Ft')

# 4. feladat
# Programunk kérje be az Euró árfolyamát (1 € hány Ft-ot ér), majd azt, hogy hány eurót akarunk átváltani Ft-ba,
# majd írja ki, hogy hány Ft az átváltott euró. (euro)

# eu_arfolyam = int(input('Kérem adja meg az EUR/Ft árfolyamát: '))
# atvalt_osszeg = int(input('Kérem adja meg az átváltandó összeget (EUR): '))
# kapott_ft = eu_arfolyam * atvalt_osszeg
# print(f'Az átváltott EUR: {kapott_ft} Ft')

# 5. feladat
# Írjunk programot, amely bekéri egy téglalap oldalait, és kiszámolja a kerületét és területét! (teglalap_ker_ter)

# a = float(input('Kérem adja meg a téglalap egyik oldalát (cm): '))
# b = float(input('Kérem adja meg a téglalap másik oldalát (cm): '))
# terulet = a * b
# kerulet = 2 * (a + b)
# print(f'Terület: {terulet} cm\nKerület: {kerulet} cm')

# 6. feladat
# Irjunk programot, amely bekéri egy kör sugarát, és kiszámolja a kör kerületét és területét! (kor_ker_ter)

# import math
# sugar = int(input('Kérem adja meg a kör sugarát: '))
# kerulet = 2 * sugar * math.pi
# terulet = math.pow(sugar, 2) * math.pi
# print(f'A kör kerülete: {kerulet}\nA kör területe: {terulet}')

# 7. feladat
# Írjunk programot a Pitagorasz-tétel alkalmazására! A program kérje be egy derékszögű háromszög két
# befogóját, és számítsa ki az átfogó hosszát! (pitagorasz)

# import math
# befogo1 = int(input('Kérem adja meg az egyik befogó hosszát:'))
# befogo2 = int(input('Kérem adja meg a másik befogó hosszát:'))
# atfogo = math.sqrt(befogo1 ** 2 + befogo2 ** 2)
# print(f'Az átfogó hossza: {atfogo}')

# 8. feladat
# Programunk kérje be a megtett út hosszát és az eltelt időt, és számítsa ki az átlagsebességet! (atlagsebesseg)


# 9. feladat
# Programunk kérje be egy autó fogyasztását (literben 100 km-en), a benzin literenkénti árát és a megteendő
# út hosszát, majd számítsa ki az útiköltséget! (uzemanyag)


# 10. feladat
# Kérjük be a felhasználó tömegét kg-ban és magasságát cm-ben, majd számítsuk ki és írjuk a képernyőre a
# felhasználó testtömegindexét az alábbi képlet alapján! TTI=𝒕ö𝒎𝒆𝒈/𝒎𝒂𝒈𝒂𝒔𝒔á𝒈𝟐
# Figyelj rá, hogy a képletben a magasság méterben megadott értékével kell számolni! (testtomegindex)



# 11. feladat
# Zöldséges standunkon háromféle terméket árulunk: almát, szilvát és szőlőt. A program írja ki a gyümölcs
# nevét és kilogrammonkénti egységárát, majd kérdezze meg, hogy mennyit szeretnénk vásárolni. A vásárolt
# mennyiség mellett jelenjen meg a fizetendő összeg, majd a végösszeget is adjuk meg! (zoldseges)


# 12. feladat
# Programunk kérje be egy hordó és egy kancsó térfogatát literekben mérve egész számként! Szeretnénk
# tudni, hogy hány teli kancsó mérhető ki a hordóból, mennyi víz marad a hordóban a teli kancsók kimerése
# után. Mennyi a hordó és a kancsó térfogatának hányadosa? (hordo)



# 13. feladat
# A bankjegyautomatából az ügyfél legfeljebb 300 000 Ft-ot vehet föl, 1 000, 5 000 és 10 000 Ft-os
# címletekben. A program kérjen be egy ezerrel osztható összeget, majd határozza meg, hogy egy beolvasott
# összeget milyen címletekben kell kifizetni, ha a lehető legkevesebb bankjegyet akarjuk felhasználni. (bankjegy)
# A megoldást a következő formában írja ki:



# 14. feladat
# Programunk kérje be egy eszköz másodpercekben mért üzemidejét! Eredményként adja meg …nap …óra
# …másodperc formában az üzemidőt! (uzemido)


# 15. feladat
# Írjunk programot, amely kiszámítja egy autóval megtett útra fizetett költségtérítést! A program kérje be a
# megtett út hosszát km-ben, az autó fogyasztását 100 km-en literben valamint az üzemanyag árát és ezek
# ismeretében számítsa ki az üzemanyagköltséget. A megtett útra, a fogyasztásra , és az üzemanyag árára is
# fogadjon el tört számokat is.
# [Az üzemanyagköltség kiszámítására használd az alábbi képletet: üzemanyagköltség=(út*fogyasztás*üzemanyag ár)/100 ]
# A költségtérítés összege 100 km-nél nem hosszabb út esetén maga az üzemanyagköltség, ennél hosszabb
# út esetén az üzemanyagköltséghez hozzáadják a megtett út 25-szörösét és így kapjuk meg a költségtérítést.
# A program címe "Utazási költségtérítés" legyen és minta szerinti formában írja ki az adatokat! (utazasikoltseg)


# Elágazások

# 16. feladat
# Kérjük be a külső hőmérsékletet, és írassuk ki, ha fagy odakint! (fagy)

# homerseklet = float(input('Kérem adja meg a külső hőmérsékletet: '))
# if homerseklet < 0:
#     print('Fagy odakint.')

# 17. feladat
# Kérdezzük meg a felhasználótól, hogy szeret-e programozni, ha igen, akkor írassunk ki, hogy „Még sokra
# viszed az életben!”, majd köszönjön el a program (Viszontlátásra!). (kerdes)

# kerdes = input('Szeret programozni?\n ')
# if kerdes == 'igen':
#     print('Még sokra viszed az életben!\nViszontlátásra!')

# 18. feladat
# Kérjünk be egy egész számot, és írassuk ki hogy az adott szám páros-e vagy sem. (paritas)

# szam = int(input('Kérek egy egész számot: '))
# if szam % 2 == 0:
#     print('Páros')
# else:
#     print('Páratlan')

# 19. feladat
# Olvassunk be egy számot a billentyűzetről, és írjuk ki, hogy osztható-e 3-mal! (oszthato3)

# szam = int(input('Kérek egy számot: '))
# if szam % 3 == 0:
#     print('Osztható hárommal.')

# 20. feladat
# Olvasson be a billentyűzetről egy számot és mondjuk meg, hogy a szám negatív, vagy pozitív vagy egyik
# sem! (elojel)

# szam = int(input('Kérek egy számot: '))
# if szam < 0:
#     print('A szám negatív.')
# elif szam > 0:
#     print('A szám pozitív.')
# else:
#     print('A szám nulla.')

# 21. feladat
# Két beolvasott számot írassunk ki úgy, hogy közéjük tesszük a megfelelő relációs jelet (<,>,=)! (relacio)

# szam1 = int(input('Kérek egy számot: '))
# szam2 = int(input('Kérem egy másik számot: '))
# if szam1 > szam2:
#     print(f'{szam1} > {szam2}')
# elif szam1 < szam2:
#     print(f'{szam1} < {szam2}')
# else:
#     print(f'{szam1} = {szam2}')

# 22. feladat
# Egy beolvasott számról döntse el a program hogy -30 és 40 között van-e! (kozotte)


# 23. feladat
# Írjunk programot,amely értékel egy dolgozatot pontszám alapján! Az értékelés a következő táblázat alapján történjen:
# Pontszám Értékelés
# 0 - 42 elégtelen
# 43 - 57 elégséges
# 58 - 72 közepes
# 73 - 87 jó
# 88 - 100 jeles



# 24. feladat
# Írj programot, amely bekér a felhasználótól egy helységnevet, valamint ennek a helységnek a lélekszámát,
# és a megadott lélekszámtól függően kiírja, hogy az adott helység milyen településtípusba tartozik.
# (telepules)
#  ha a lélekszám kevesebb, mint 5000, akkor község
#  ha a lélekszám legalább 5000, de kevesebb, mint 20 000, akkor kisváros
#  ha a lélekszám legalább 20 000, de kevesebb, mint 100 000, akkor középváros
#  ha a lélekszám legalább 100 000, de kevesebb, mint 1 000 000, akkor nagyváros
#  ha a lélekszám legalább 1 000 000, akkor metropolis
#  ha a felhasználó 0 vagy annál kisebb számot ad meg, a program írja ki, hogy "Hibás adatbevitel"



# 25. feladat
# A program kérjen be két számot, és egy műveleti jelet (+,-,/,*), majd írja ki a művelet eredményét.
# (muvelet)


# 26. feladat
# Kérjük be egy diák matematika év végi jegyét numerikus formában, és írjuk ki azt szövegesen (elégtelen,
# elégséges, közepes, jó, jeles). Amennyiben a beírt érdemjegy nem 1..5 közötti szám, úgy a hibás adat kiírás
# jelenjen meg. (osztalyzat)



# 27. feladat
# Kérjük be egy nap sorszámát (1..7) numerikus formában, és írjuk ki a nap megnevezését a képernyőre
# (hétfő, kedd, ..., vasárnap). Amennyiben a beírt sorszám nem 1..7 közötti szám, úgy a hibás adat kiírás
# jelenjen meg. (hetnapjai)

# day_number = int(input('Kérem adja meg a nap sorszámát: '))
# weeks = ['Hétfö', 'Kedd', 'Szerda', 'Csütörtök', 'Péntek', 'Szombat', 'Vasárnap']
# if 0 < day_number < 8:
#     print(weeks[day_number - 1])
# else:
#     print('Hibás adat.')

# 28. feladat
# Kérjük be egy hónap sorszámát (1..12) numerikus formában, és írjuk ki a hónap megnevezését a képernyőre
# (január, ..., december). Amennyiben a beírt sorszám nem 1..12 közötti szám, úgy a hibás adat kiírás jelenjen
# meg. (honapok)



# 29. feladat
# Kérjük be egy áru egységárát (Ft), a vásárlandó mennyiséget (db), és hogy mennyi pénz van nálunk (Ft).
# Adjuk meg, hogy meg tudjuk-e vásárolni a kívánt darabszámot, és ez esetben mennyi pénzünk maradna a
# vásárlás után. Ha nincs elég pénzünk, akkor azt adjuk meg, hány darab termék megvásárlására lenne csak
# elég a pénzünk. (vasarlas)



# 30. feladat
# Adott évről döntsük el, hogy szökőév-e! (Szökőévek a következők: minden néggyel osztható év, kivéve a
# százzal is oszthatókat. Szökőévek viszont a 400-zal osztható évek. Vagyis a százasra végződő évek közül
# csak azok szökőévek, amelyek 400-zal is oszthatók.) (szokoev)




# Véletlenszámok


# 31. feladat
# Generáljunk háromjegyű véletlenszámot! (haromjegyu)

# import random as r
# veletlenszam = r.randint(100, 999)
# print(veletlenszam)

# 32. feladat
# Programunk adjon meg véletlenszerűen egy 0 és 25 közötti egész számot, illetve egy 0 és 25 közötti
# tizedestörtet! (veletlenszam1)

# import random as r
# vlszam = int(r.randint(0, 25))
# print(vlszam)
# vlszam = float(r.randint(0, 25))
# print(vlszam)

# 33. feladat
# Programunk adjon meg véletlenszerűen egy 15 és 25 közötti egész számot, illetve egy 15 és 25 közötti
# tizedestörtet! (veletlenszam2)

# import random as r
# vlszam = int(r.randint(15, 25))
# print(vlszam)
# vlszam = float(r.randint(15, 25))
# print(vlszam)

# 34. feladat
# Programunk adjon meg egy 0-nál nem kisebb, de 100-nál kisebb tetszőleges páros számot! (veletlen_paros)

# import random as r
# vlszam = 1
# while vlszam % 2 != 0:
#     vlszam = r.randint(0, 100)
# print(vlszam)


# 35. feladat
# Generáljunk a [100,200] tartományból egy 5-tel osztható számot! (veletlen_5)

# import random as r
# vlszam = 1
# while vlszam % 5 != 0:
#     vlszam = r.randint(100, 200)
# print(vlszam)

# 36. feladat
# Tetszőleges 0 és egymillió közötti egész számról mondja meg a program hogy hány jegyű! (hanyjegyu)

'''
import random as r
vlszam = int(r.randint(0, 1000000))
'''

# 37. feladat
# Generáljunk 6 kockadobást! (kockadobas)



# 38. feladat
# Generáljunk véletlenszerűen 5 különböző lottószámot! (lotto)



# 39. feladat
# A program találjon ki két véletlen számot 10..50 között, majd írja ki őket a képernyőre A+B=? formában
# (A és B helyébe a konkrét érték kerüljön behelyettesítésre. A program kérje a választ a felhasználótól, és
# adja meg, hogy a beírt érték valóban a két szám összege-e vagy sem. (osszead)



# 40. feladat
# Programunk generáljon egy 0-100 közti egész számot, majd kérjen a felhasználótól is egy ilyet. Ha a két
# szám megegyezik, akkor jelenjen meg a „nyert”, egyébként a „nem nyert” szöveg! (szamkitalalo)