# 1.lap_Kiíratás, adatbekérés billentyűzetről, változók, matematikai műveletek

# 1. feladat
# Programunk kérje be egy ember lakhelyének irányítószámát, a várost, a közterület nevét, a közterület jellegét,
# a házszámot és végül írja ki egy sorban a következő formátumban: Pl.: 1042 Budapest Tanoda tér 2. (lakcim)
'''
irszam = input("Kérem adja meg az irszámát: ")
telepules = input("Kérem adja meg a települését: ")
kozterneve = input("Kérem adja meg az közterület nevét: ")
kozter_jellege = input("Kérem adja meg az közterület jellegét: ")
hazszam = input("Kérem adja meg a házszámát: ")

print(f'{irszam} {telepules} {kozterneve} {kozter_jellege} {hazszam}.')  '''

# 2. feladat
# Olvassunk be két vezeték- és két keresztnevet, és írassuk ki az ezekből képezhető neveket! (nevek)
'''
import math
v_nev1 = input("Kérem adjon meg egy vezetéknevet: ")
v_nev2 = input("Kérem adjon meg egy másik vezetéknevet: ")
k_nev1 = input("Kérem adjon meg egy keresztnevet: ")
k_nev2 = input("Kérem adjon meg egy másik keresztnevet: ")

print(f'{v_nev1} {k_nev1}, {v_nev1} {k_nev2}, {v_nev2} {k_nev1}, {v_nev2} {k_nev2}')   '''

# 3. feladat
# Olvassuk be a havi fizetést, és eredményként írassuk ki az éves fizetést! Milyen típusú változókat használhatunk? (fizetes)
'''
haviber = int(input(f'Kérem adja meg a havi bérét: '))

print(f'Éves bér: {haviber*12} Ft')   '''

# 4. feladat
# Programunk kérje be az Euró árfolyamát (1 € hány Ft-ot ér), majd azt, hogy hány eurót akarunk átváltani Ft-ba,
# majd írja ki, hogy hány Ft az átváltott euró. (euro)
'''
euro_arfolyam = int(input('Kérem adja meg az euró árfolyamát: '))
atvalt = int(input('Kérem adja meg az átváltandó összeget: '))

print(f'Az átváltott Euró: {euro_arfolyam * atvalt} Ft')   '''

# 5. feladat
# Írjunk programot, amely bekéri egy téglalap oldalait, és kiszámolja a kerületét és területét! (teglalap_ker_ter)
'''
teglalap1 = int(input('Kérem adja meg a téglalap egyik oldalának hosszát: '))
teglalap2 = int(input('Kérem adja meg a téglalap másik oldalának hosszát: '))

print(f'A téglalap kerülete: {2* (teglalap1+teglalap2)}')
print(f'A téglalap területe: {teglalap1*teglalap2}')   '''

# 6. feladat
# Irjunk programot, amely bekéri egy kör sugarát, és kiszámolja a kör kerületét és területét! (kor_ker_ter)
'''
import math
r = int(input('Kérem adja meg a kör sugarát: '))
K = 2 * r * math.pi
T = r ** 2 * math.pi

print(f'A kör kerülete: {K}\nA kör tetülete: {T}')   '''

# 7. feladat
# Írjunk programot a Pitagorasz-tétel alkalmazására! A program kérje be egy derékszögű háromszög két
# befogóját, és számítsa ki az átfogó hosszát! (pitagorasz)
'''
import math
a = float(input('Kérem adja meg az egyik befogót:'))
b = float(input('Kérem adja meg az másik befogót:'))
c =math.sqrt(a ** 2 + b ** 2)

print(f'Az átfogó: {c}')  '''

# 8. feladat
# Programunk kérje be a megtett út hosszát és az eltelt időt, és számítsa ki az átlagsebességet! (atlagsebesseg)
'''
megtett_ut = float(input('Kérem adja meg az út hosszát: '))
eltelt_ido = float(input('Kérem adja meg az eltelt időt: '))
atlagseb = megtett_ut // eltelt_ido

print(f'Átlagsebesség: {atlagseb} km/h')   '''

# 9. feladat
# Programunk kérje be egy autó fogyasztását (literben 100 km-en), a benzin literenkénti árát és a megteendő
# út hosszát, majd számítsa ki az útiköltséget! (uzemanyag)
'''
fogyasztas = float(input('Kérem adja meg az autó fogyasztását (l): '))
benzinar = int(input('Kérem adja meg a benzin árát (Ft): '))
uthossza = float(input('Kérem adja meg az út hosszát (km): '))
utikoltseg = uthossza / 100 * fogyasztas * benzinar

print(f'Útiköltség: {utikoltseg} Ft')   '''

# 10. feladat
# Kérjük be a felhasználó tömegét kg-ban és magasságát cm-ben, majd számítsuk ki és írjuk a képernyőre a
# felhasználó testtömegindexét az alábbi képlet alapján! TTI=𝒕ö𝒎𝒆𝒈/𝒎𝒂𝒈𝒂𝒔𝒔á𝒈𝟐
# Figyelj rá, hogy a képletben a magasság méterben megadott értékével kell számolni! (testtomegindex)
'''
tomeg = float(input('Kérem adja meg a tömegét (kg):'))
magassag = float(input('Kérem adja meg a magasságát (cm):'))
ttindex = tomeg / ((magassag/100) ** 2)

print(f'Testtömegindexe: {ttindex}')   '''

# 11. feladat
# Zöldséges standunkon háromféle terméket árulunk: almát, szilvát és szőlőt. A program írja ki a gyümölcs
# nevét és kilogrammonkénti egységárát, majd kérdezze meg, hogy mennyit szeretnénk vásárolni. A vásárolt
# mennyiség mellett jelenjen meg a fizetendő összeg, majd a végösszeget is adjuk meg! (zoldseges)
'''
alma = 300
szilva = 200
szolo = 600

print(f'Alma: {alma} Ft/kg\nSzilva: {szilva} Ft/kg\nSzőlő: {szolo} Ft/kg')

alma_kg = float(input('Mennyi almát szeretne vásárolni (kg): '))
alma_ar = alma * alma_kg
print(f'Alma ára: {alma_ar} Ft/kg')
szilva_kg = float(input('Mennyi szilvát szeretne vásárolni (kg): '))
szilva_ar = szilva * szilva_kg
print(f'Szilva ára: {szilva_ar} Ft/kg')
szolo_kg = float(input('Mennyi szőlőt szeretne vásárolni (kg): '))
szolo_ar = szolo * szolo_kg
print(f'Szőlő ára: {szolo_ar} Ft/kg')
ossz = alma_ar + szilva_ar + szolo_ar
print(f'Végösszeg: {ossz} Ft')   '''

# 12. feladat
# Programunk kérje be egy hordó és egy kancsó térfogatát literekben mérve egész számként! Szeretnénk
# tudni, hogy hány teli kancsó mérhető ki a hordóból, mennyi víz marad a hordóban a teli kancsók kimerése
# után. Mennyi a hordó és a kancsó térfogatának hányadosa? (hordo)
'''
hordo = int(input('Kérem adja meg a hordó térfogatát (l): '))
kancso = int(input('Kérem adja meg a kancsó térfogatát (l): '))
teli_kancso = hordo // kancso
maradek_viz = hordo % kancso
hanyados = hordo / kancso
print(f'Kimért teli kancsó: {teli_kancso}'
      f'\nA hordóban maradt víz: {maradek_viz} l25'
      f'\nA hordó és a kancsó hányadosa: {hanyados}')   '''

# 13. feladat
# A bankjegyautomatából az ügyfél legfeljebb 300 000 Ft-ot vehet föl, 1 000, 5 000 és 10 000 Ft-os
# címletekben. A program kérjen be egy ezerrel osztható összeget, majd határozza meg, hogy egy beolvasott
# összeget milyen címletekben kell kifizetni, ha a lehető legkevesebb bankjegyet akarjuk felhasználni. (bankjegy)
# A megoldást a következő formában írja ki:

# 14. feladat
# Programunk kérje be egy eszköz másodpercekben mért üzemidejét! Eredményként adja meg …nap …óra
# …másodperc formában az üzemidőt! (uzemido)
'''
uzemido = int(input('Kérem adja meg az üzemidőt (sec): '))
eredmeny_nap = uzemido // 86400
eredmeny_ora = (uzemido % 86400) // 3600
eredmeny_sec = (uzemido % 86400) % 3600
print(f'Üzemidő: {eredmeny_nap} nap {eredmeny_ora} óra {eredmeny_sec} másodperc')  '''


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
'''
homerseklet = float(input('Kérem adja meg a kinti hőmérsékletet: '))
if homerseklet < 0:
    print(f'Fagy.')  '''

# 17. feladat
# Kérdezzük meg a felhasználótól, hogy szeret-e programozni, ha igen, akkor írassunk ki, hogy „Még sokra
# viszed az életben!”, majd köszönjön el a program (Viszontlátásra!). (kerdes)
'''
kerdes = input('Szeretsz programozni? ')
if kerdes == 'igen':
    print(f'Még sokra viszed az életben!\nViszontlátásra!')   '''

# 18. feladat
# Kérjünk be egy egész számot, és írassuk ki hogy az adott szám páros-e vagy sem. (paritas)
'''
szam = int(input('Kérem adjon meg egy számot: '))
if szam % 2 == 0:
    print(f'Páros.')
else:
    print(f'Páratlan.')   '''

# 19. feladat
# Olvassunk be egy számot a billentyűzetről, és írjuk ki, hogy osztható-e 3-mal! (oszthato3)
'''
szam = int(input('Kérem adjon meg egy számot: '))
if szam % 3 == 0:
    print(f'Osztható 3-al!')
else:
    print(f'Nem osztahtó 3-al.')   '''

# 20. feladat
# Olvasson be a billentyűzetről egy számot és mondjuk meg, hogy a szám negatív, vagy pozitív vagy egyik
# sem! (elojel)
'''
szam = int(input('Kérem adjon meg egy számot: '))
if szam < 0:
    print(f'Negatív szám.')
elif szam > 0:
    print(f'Pozitív szám.')
else:
    print(f'Egyik sem.')   '''

# 21. feladat
# Két beolvasott számot írassunk ki úgy, hogy közéjük tesszük a megfelelő relációs jelet (<,>,=)! (relacio)
'''
szam1 = input('Kérem adjon meg egy számot: ')
szam2 = input('Kérem adjon meg egy másik számot: ')
if szam1 > szam2:
    print(f'{szam1} > {szam2}')
elif szam1 < szam2:
    print(f'{szam1} < {szam2}')
else:
    print(f'{szam1} = {szam2}')   '''

# 22. feladat
# Egy beolvasott számról döntse el a program hogy -30 és 40 között van-e! (kozotte)
'''
szam = int(input('Kérem adjon meg egy számot: '))
if szam < 40 and szam > -30:
    print(f'A megadott szám -30 és 40 között van.')
else:
    print(f'Nincs közötte.')   '''

# 23. feladat
# Írjunk programot,amely értékel egy dolgozatot pontszám alapján! Az értékelés a következő táblázat alapján történjen:
# Pontszám Értékelés
# 0 - 42 elégtelen
# 43 - 57 elégséges
# 58 - 72 közepes
# 73 - 87 jó
# 88 - 100 jeles
'''
pontszam = int(input('Kérem adja meg a dolgozat pontszámát: '))
if pontszam < 42:
    print(f'Értékelése: elégtelen.')
elif 43 < pontszam < 57:
    print(f'Értékelése: elégséges.')
elif 58 < pontszam < 73:
    print(f'Értékelése: közepes.')
elif 73 < pontszam < 87:
    print(f'Értékelése: jó.')
else:
    print(f'Értékelése: jeles.')    '''

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
'''
input('Kérem adjon meg egy helységnevet: ')
lelekszam = int(input('Kérem adja meg a helység lélekszámát: '))
if 1 <= lelekszam < 5000:
    print(f'község')
elif 5000 <= lelekszam < 20000:
    print(f'kisváros')
elif 20000 <= lelekszam < 100000:
    print(f'középváros')
elif 100000 <= lelekszam < 1000000:
    print(f'nagyváros')
elif 1000000 <= lelekszam:
    print(f'metropolis')
else:
    print(f'Hibás adatbevitel.')   '''

# 25. feladat
# A program kérjen be két számot, és egy műveleti jelet (+,-,/,*), majd írja ki a művelet eredményét.
# (muvelet)
'''
szam1 = int(input('Kérem adjon meg egy számot: '))
szam2 = int(input('Kérem adjon meg egy másik számot: '))
jel = input('Kérem adjon meg egy műveleti jelet (+,-,/,*): ')
if jel == "+":
    print(szam1+szam2)
elif jel == "-":
    print(szam1-szam2)
elif jel == "/":
    print(szam1/szam2)
elif jel == "*":
    print(szam1*szam2)  '''

# 26. feladat
# Kérjük be egy diák matematika év végi jegyét numerikus formában, és írjuk ki azt szövegesen (elégtelen,
# elégséges, közepes, jó, jeles). Amennyiben a beírt érdemjegy nem 1..5 közötti szám, úgy a hibás adat kiírás
# jelenjen meg. (osztalyzat)
'''
jegy = int(input('Kérem adja meg a matek év végi jegyét: '))
if jegy == 1:
    print(f'Értékelése: elégtelen')
elif jegy == 2:
    print(f'Értékelése: elégséges')
elif jegy == 3:
    print(f'Értékelése: közepes')
elif jegy == 4:
    print(f'Értékelése: jó')
elif jegy == 5:
    print(f'Értékelése: jeles')
else:
    print(f'Hibás adat.')   '''

# 27. feladat
# Kérjük be egy nap sorszámát (1..7) numerikus formában, és írjuk ki a nap megnevezését a képernyőre
# (hétfő, kedd, ..., vasárnap). Amennyiben a beírt sorszám nem 1..7 közötti szám, úgy a hibás adat kiírás
# jelenjen meg. (hetnapjai)
'''
sorszam = int(input('Kérem adja egy nap sorszámát: '))
if sorszam == 1:
    print(f'Ez a hétfő.')
elif sorszam == 2:
    print(f'Ez a kedd.')
elif sorszam == 3:
    print(f'Ez a szerda.')
elif sorszam == 4:
    print(f'Ez a csütörtök.')
elif sorszam == 5:
    print(f'Ez a péntek.')
elif sorszam == 6:
    print(f'Ez a szombat.')
elif sorszam == 7:
    print(f'Ez a vasárnap.')
else:
    print(f'Hibás adat.')   '''

# 28. feladat
# Kérjük be egy hónap sorszámát (1..12) numerikus formában, és írjuk ki a hónap megnevezését a képernyőre
# (január, ..., december). Amennyiben a beírt sorszám nem 1..12 közötti szám, úgy a hibás adat kiírás jelenjen
# meg. (honapok)
'''
sorszam = int(input('Kérem adja egy hónap sorszámát: '))
if sorszam == 1:
    print(f'Ez a január.')
elif sorszam == 2:
    print(f'Ez a február.')
elif sorszam == 3:
    print(f'Ez a március.')
elif sorszam == 4:
    print(f'Ez a április.')
elif sorszam == 5:
    print(f'Ez a május.')
elif sorszam == 6:
    print(f'Ez a június.')
elif sorszam == 7:
    print(f'Ez a július.')
elif sorszam == 8:
    print(f'Ez a augusztus.')
elif sorszam == 9:
    print(f'Ez a szeptember.')
elif sorszam == 10:
    print(f'Ez a október.')
elif sorszam == 11:
    print(f'Ez a november.')
elif sorszam == 12:
    print(f'Ez a december.')
else:
    print(f'Hibás adat.')   '''

'''
month = int(input('Kérem adja meg egy hónap sorszámát: '))
months = ["január", "február", "március",
          "április", "május", "június",
          "július", "augusztus", "szeptember",
          "október", "november", "december"]
print(months[month-1])
'''

# 29. feladat
# Kérjük be egy áru egységárát (Ft), a vásárlandó mennyiséget (db), és hogy mennyi pénz van nálunk (Ft).
# Adjuk meg, hogy meg tudjuk-e vásárolni a kívánt darabszámot, és ez esetben mennyi pénzünk maradna a
# vásárlás után. Ha nincs elég pénzünk, akkor azt adjuk meg, hány darab termék megvásárlására lenne csak
# elég a pénzünk. (vasarlas)
'''
ar = int(input('Kérem adja meg az egységárat (Ft): '))
mennyiseg = int(input('Kérem adja a vásárlandó mennyiséget (db): '))
penz = int(input('Kérem adja meg az önnél lévő pénzmennyiséget (Ft): '))



'''

# 30. feladat
# Adott évről döntsük el, hogy szökőév-e! (Szökőévek a következők: minden néggyel osztható év, kivéve a
# százzal is oszthatókat. Szökőévek viszont a 400-zal osztható évek. Vagyis a százasra végződő évek közül
# csak azok szökőévek, amelyek 400-zal is oszthatók.) (szokoev)



# Véletlenszámok
# 31. feladat
# Generáljunk háromjegyű véletlenszámot! (haromjegyu)
'''
import  random as r
print(r.randint(100, 999))   '''

# 32. feladat
# Programunk adjon meg véletlenszerűen egy 0 és 25 közötti egész számot, illetve egy 0 és 25 közötti
# tizedestörtet! (veletlenszam1)
'''
import random as r
print(r.randint(0,25))
print(float(r.randint(0,25)))   '''

# 33. feladat
# Programunk adjon meg véletlenszerűen egy 15 és 25 közötti egész számot, illetve egy 15 és 25 közötti
# tizedestörtet! (veletlenszam2)
'''
import random as r
print(r.randint(15,25))
print(float(r.randint(15,25)))   '''

# 34. feladat
# Programunk adjon meg egy 0-nál nem kisebb, de 100-nál kisebb tetszőleges páros számot! (veletlen_paros)
'''
import random
vszam = 1
while vszam % 2 != 0:
     vszam = random.randint(0, 100)
print(f'Páros véletlen szám: {vszam}')   '''

# 35. feladat
# Generáljunk a [100,200] tartományból egy 5-tel osztható számot! (veletlen_5)
'''
import random
vszam = 1
while vszam % 5 != 0:
     vszam = random.randint(100, 200)
print(f'Öttel osztható szám: {vszam}')  '''

# 36. feladat
# Tetszőleges 0 és egymillió közötti egész számról mondja meg a program hogy hány jegyű! (hanyjegyu)
'''
import random
vszam = random.randint(0,1000000)
print(vszam)
if 0 < vszam < 10:
     print(f'A szám egyjegyű.')
elif 9 < vszam < 100:
     print(f'A szám kétjegyű.')
elif 99 < vszam < 1000:
     print(f'A szám háromjegyű.')
elif 999 < vszam < 10000:
     print(f'A szám négyjegyű.')
elif 9999 < vszam < 100000:
     print(f'A szám ötjegyű.')
else:
     print(f'A szám hatjegyű.')   '''

# vagy
'''
import random as rng
num = rng.randint(0, 1000000)
print(f'A szám: {num}\n{len(str(num))} jegyű.')
'''
# 37. feladat
# Generáljunk 6 kockadobást! (kockadobas)
'''
import random
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))  '''

# vagy
'''
import random as rng
for x in range(6):
    print(f'{x + 1}.dobás: {rng.randint(1, 6)}')
'''
# 38. feladat
# Generáljunk véletlenszerűen 5 különböző lottószámot! (lotto)
'''
import random
print(random.randint(1,90))
print(random.randint(1,90))
print(random.randint(1,90))
print(random.randint(1,90))
print(random.randint(1,90))   '''

# 39. feladat
# A program találjon ki két véletlen számot 10..50 között, majd írja ki őket a képernyőre A+B=? formában
# (A és B helyébe a konkrét érték kerüljön behelyettesítésre. A program kérje a választ a felhasználótól, és
# adja meg, hogy a beírt érték valóban a két szám összege-e vagy sem. (osszead)
'''
import random
vszam1 = random.randint(10,50)
vszam2 = random.randint(10,50)
keplet = vszam1 + vszam2
valasz = int(input(f'Kérem adja meg a megoldást: {vszam1} + {vszam2} = '))
if valasz == keplet:
    print(f'helyes')
else:
    print(f'helytelen, a helyes megoldás: {keplet}')   '''

# 40. feladat
# Programunk generáljon egy 0-100 közti egész számot, majd kérjen a felhasználótól is egy ilyet. Ha a két
# szám megegyezik, akkor jelenjen meg a „nyert”, egyébként a „nem nyert” szöveg! (szamkitalalo)
'''
import random
vszam = random.randint(0,100)
print(vszam)
szam = int(input(f'Kérem adjon meg egy számot 0 és 100 között: '))
if vszam == szam:
     print(f'nyert')
else:
     print(f'nem nyert')   '''