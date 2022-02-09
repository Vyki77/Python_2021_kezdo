# 1. feladat
# Írassuk ki a képernyőre a nevünket egymás alá 10-szer. (nev10)
'''
for nev in range(10):
    print('Viki')
'''
# 2. feladat
# Kérjünk be egy számot a billentyűzetről (n), valamint egy szöveget és írjuk ki n-szer a megadott szöveget egymás
# mellé szóközökkel elválasztva. (ismetlesN)
'''
n = int(input('Kérek egy számot: '))
szoveg = input('Kérek egy szöveget:')
for i in range(n):
    print(f'{szoveg}', end=" ")
'''




# 7. Írassuk ki a képernyőre 0-tól 30-ig a számok négyzetét! (negyzetszamok)
'''
import math
szam = 1
while szam <= 30:
    print(f'{szam} négyzete = ',int(math.pow(szam, 2)))
    szam += 1
'''
# vagy
'''
for x in range(0, 31):
    print(f'{x} négyzete: {x * x}')
'''
# 8. Írassuk ki a képernyőre a 2 első 30 hatványát! (2hatvanyok)
'''
import math
hatvany = 1
while hatvany <= 30:
    print(f'2 a(z) {hatvany} hatványon = ',int(math.pow(2, hatvany)))
    hatvany += 1
'''
# 9. Írassuk ki a képernyőre a 100-nál nem nagyobb páratlan számokat! (paratlan)
'''
for szam in range(0, 101):
    if szam % 2 == 1:
        print(szam)
'''
# 10. Írassuk ki a képernyőre a 100-nál nem nagyobb páratlan számokat csökkenő sorrendben! (paratlan2)
'''
for szam in range(100, 0, -1):
    if szam % 2 == 1:
        print(szam)
'''
#11. Írassuk ki a képernyőre annak a sorozatnak az első 50 tagját, ami 10-zel kezdődik és 7-tel növekszik.(szamtanisor1)
'''
novekvo = 10
szam = 0
while szam < 50:
    print(novekvo)
    szam += 1
    novekvo += 7
'''
#15. Írjunk programot, ami kiírja a képernyőre az összes 3-mal osztható kétjegyű számot! (ketjegyu3)
'''
for x in range(10, 100):
    if x % 3 == 0:
        print(x)
'''
# 16. Írassuk ki a képernyőre egy billentyűzetről megadott szám összes osztóját! (osztok)
'''
szam = int(input('Kérek egy számot: '))
for x in range(1, szam + 1):
    if szam % x == 0:
        print(x)
'''
# 18. Állapítsuk meg két billentyűzetről bekért számról, hogy mi a legnagyobb közös osztójuk!
# (A legnagyobb olyan szám, amely mindkét számot osztja.) (lnko)
'''
szam1 = int(input('Kérem az elsö számot: '))
szam2 = int(input('Kérem a második számot: '))
lko = 0
for x in range(1, max(szam1, szam2) + 1):
    if szam1 % x == 0 and szam2 % x == 0:
        lko = x
print(lko)
'''
# 19. Írjunk programot, amely kiírja az összes háromjegyű számot, amelynek az első és utolsó számjegye egyforma! (szim3jegyu)
'''
for x in range(100, 1000):
    if str(x)[0] == str(x)[-1]:
        print(x)
'''
#18. feladat
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
    print(f'Nem osztahtó 3-al.') 
'''
# 28. feladat
# Kérjük be egy hónap sorszámát (1..12) numerikus formában, és írjuk ki a hónap megnevezését a képernyőre
# (január, ..., december). Amennyiben a beírt sorszám nem 1..12 közötti szám, úgy a hibás adat kiírás jelenjen
# meg. (honapok)
'''
month = int(input('Kérem adja meg egy hónap sorszámát: '))
months = ["január", "február", "március",
          "április", "május", "június",
          "július", "augusztus", "szeptember",
          "október", "november", "december"]
print(months[month-1])
'''
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
print(f'Öttel osztható szám: {vszam}')  
'''
# 36. feladat
# Tetszőleges 0 és egymillió közötti egész számról mondja meg a program hogy hány jegyű! (hanyjegyu)
'''
import random as rng
num = rng.randint(0, 1000000)
print(f'A szám: {num}\n{len(str(num))} jegyű.')
'''
