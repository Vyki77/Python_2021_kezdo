# 2. lap_ Számlálós ciklus (for ciklus)
# 1. feladat
# Írassuk ki a képernyőre a nevünket egymás alá 10-szer. (nev10)
'''
for nev in range(10):
    print('Viki')   '''

# 2. feladat
# Kérjünk be egy számot a billentyűzetről (n), valamint egy szöveget és írjuk ki n-szer a megadott szöveget egymás
# mellé szóközökkel elválasztva. (ismetlesN)
'''
n = int(input('Kérem adjon meg egy számot: '))
szoveg = str(input('Kérem írjon egy szöveget: '))
for i in range(n):
    print(f'{szoveg}',end=" ")
'''
# 3. feladat
# Számoljon vissza a program 10-től egyesével (mondjuk másodpercenként), majd írja ki, hogy lejárt az időd és
# kis idő múlva lépjen ki! (visszaszamol)
# 4. feladat
# Mozogjon a nevünk a képernyőn ! (nev_mozog)
# 5. feladat
# Írassunk ki a képernyőre 200 csillagot véletlenszerűen kiválasztott helyekre. (randomcsillag)
# 6. feladat
# Az előbbi feladatban állítsuk be véletlenszerűen a csillagok színeit (a Console-ablakban 16 szín közül
# választhatunk.) (randomszin)

# 7. feladat
# Írassuk ki a képernyőre 0-tól 30-ig a számok négyzetét! (negyzetszamok)
'''
szam = 0
while szam <= 30:
    negyzet = szam ** 2
    print(negyzet)
    szam += 1   '''

# 8. feladat
# Írassuk ki a képernyőre a 2 első 30 hatványát! (2hatvanyok)
'''
hatvany = 1
while hatvany <= 30:
    keplet = 2 ** hatvany
    print(keplet)
    hatvany += 1   '''

# 9. feladat
# Írassuk ki a képernyőre a 100-nál nem nagyobb páratlan számokat! (paratlan)


for szam in range(100):
    print(szam)

# 10. feladat
# Írassuk ki a képernyőre a 100-nál nem nagyobb páratlan számokat csökkenő sorrendben! (paratlan2)

# 11. feladat
# Írassuk ki a képernyőre annak a sorozatnak az első 50 tagját, ami 10-zel kezdődik és 7-tel növekszik.
# (szamtanisor1)

# 12. feladat
# Kérjük be a felhasználótól egy számtani sorozat első tagját és a differenciáját. A program írja ki a sorozat első
# 20 tagját! (szamtanisor2)

# 13. feladat
# Kérjük be a felhasználótól egy számtani sorozat két szomszédos tagját. A program írja ki a sorozat előző és
# következő 10 tagját! (szamtanisor3)

# 14. feladat
# Készítsünk programot, amely -30 °C-tól +30°C-ig kiírja a hőmérsékletet Fahrenheit fok egységekben!
# (F=1,8*C+32) (homerseklet_atvaltas)

# 15. feladat
# Írjunk programot, ami kiírja a képernyőre az összes 3-mal osztható kétjegyű számot! (ketjegyu3)

# 16. feladat
# Írassuk ki a képernyőre egy billentyűzetről megadott szám összes osztóját! (osztok)

# 17. feladat
# Döntsük el egy számról, hogy prím-e! Ha nem az, adjuk meg egy valódi osztóját! (prim_teszt)

# 18. feladat
# Állapítsuk meg két billentyűzetről bekért számról, hogy mi a legnagyobb közös osztójuk! (A legnagyobb olyan
# szám, amely mindkét számot osztja.) (lnko)

# 19. feladat
# Írjunk programot, amely kiírja az összes háromjegyű számot, amelynek az első és utolsó számjegye egyforma!
# (szim3jegyu)

# 20. feladat
# Számoljuk ki és írjuk ki a képernyőre a Fibonacci sorozat első 10 elemét! A sorozat első két eleme 1-es, ezután
# pedig mindig úgy kapjuk a sorozat következő elemét, hogy az utolsó két elemet összeadjuk. Formálisan leírva:
# a1 = 1
# a2 = 1
# an = an-1 + an-2, ha n>2
# (fibonacci)

# 21. feladat
# Keresd meg program segítségével az Armstrong-számokat, vagyis azokat a háromjegyű számokat, amelyeknek
# a jegyeit külön-külön a harmadikra hatványozva és ezeket összeadva az eredeti számot kapjuk vissza!
# (armstrong)

# 22. feladat
# Kérjünk be a billentyűzetről egy számot, és írjuk ki a faktoriálisát! Pl. 5!=1*2*3*4*5=120 (faktor)

# 23. feladat
# Feldobunk egy dobókockát 100-szor. Írjunk programot, amely megszámolja, hány 6-os dobás volt a 100 dobás
# között! (6dobas)

# 24. feladat
# Feldobunk két dobókockát 20-szor. Hányszor dobtunk összesen 12-t? (dobasosszeg10)

# 25. feladat
# Írassuk ki a képernyőre az első 100 természetes szám összegét! (sorosszeg)

# 26. feladat
# Feldobunk egy dobókockát 100-szor. Írjunk programot, megadja a dobott számok összegét! (dobasosszeg)

# 27. feladat
# Kérjünk be egy tetszőleges szöveget, és írassuk ki fordítva! (szoveg_forditva)

# 28. feladat
# Írassuk ki a nevünket átlósan. (nev_atlosan)