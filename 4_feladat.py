# 1.feladat - Írjuk ki „ritkítva” a nevünket (minden karakter után tegyünk egy szóközt).
'''
nev = 'Nagy Viktória'
for karakter in nev:
    print(karakter, end=' ')
'''

# 2.feladat -  Írassuk ki a nevünket függőlegesen!
'''
nev = 'Nagy Viktória'
for karakter in nev:
    print(karakter)
'''
# 3.feladat -Írassuk ki a nevünket átlósan!
'''
nev = 'Nagy Viktória'
szokozokSzama = 0
for k in nev:
    print(f'{ szokozokSzama * " "}{ k }')
    szokozokSzama += 1

#vagy_ ez a jobb

for i in range(0, len(nev) - 1):
    print(f'{i * " "}{nev[i]}')
'''
# 4. Kérjünk be egy szót, majd írjuk ki * karakterekkel bekeretezve!
'''
szo = input('Kérem adjon meg egy szót: ')
print(f'{(len(szo) + 2) * "*"}\n'
        f'*{szo}*\n'
        f'{(len(szo) + 2) * "*"}\n')
'''
# 5. Kérjünk be egy tetszőleges szöveget, és írassuk ki fordítva!
'''
szoveg = input('Kérem adjon meg egy szöveget: ')
i = len(szoveg) - 1
while i >= 0:
    print(szoveg[i], end='')
    i -= 1
#vagy


for i in range(len(szoveg) - 1, -1, -1):
    print(szoveg[i], end='')
    i -= 1
    
'''
# 6. Kérjünk be egy tetszőleges szöveget, és számoljuk meg, hogy hány "e" betű van benne!

#szoveg = input('Kérem adjon meg egy szöveget: ')
#print(szoveg.count('e'))
'''
db = 0
for k in szoveg:
    if k == 'e':
        db += 1
print(f'Az \'e\' betük száma: {db}')

'''
# 7. Számoljuk meg egy szövegben szereplő szavakat!
'''
szoveg = input('Kérem adjon meg egy szöveget: ')
szavakSzama = len(szoveg.split(' '))
print(f'A szavak száma: {szavakSzama}')

'''
# 8. Döntsd el a beírt mondat típusát! (kijelentő/kérdő/felszólító)
'''
mondat = input('Kérem adjon meg egy mondatot: ')
if mondat.endswith('.'):
    print('Ez a mondat kijelentő')
elif mondat.endswith('?'):
    print('Ez a mondat kérdő')
else:
    print('Ez a mondat felkiáltó / felszólító / óhajtó')
'''
# 9. Írassunk ki egy szöveget csupa nagybetűvel/ kisbetűvel.
'''
szoveg = input('Kérem adjon meg egy szöveget: ')
print(szoveg.upper())
print(szoveg.lower())

'''
# 10. Kérjünk be egy szót, és cseréljük le az első karakterét nagybetűre

#szo = input('Kérem adjon meg egy szót: ')
#print(szo.capitalize())
'''
print(f'{szo[0].upper()}{szo[1:]}')
'''
# 11. Döntsük el, hogy van-e egy szóban "j" betű !
'''
szo = input('Kérem adjon meg egy szót: ')
vanE = False
for k in szo:
    if k == 'j':
        vanE = True

#print(szo.__contains__('j'))

#vagy ez a jobb

print('j' in szo)

'''
# 12. Döntsük el, hogy van-e egy szóban "ly" betű !

'''
szo = input('Kérem adjon meg egy szót: ')
vanE = False
for k in szo:
    if k == 'ly':
        vanE = True
print('ly' in szo)
'''
# 13. Számoljuk meg egy szóban a magánhangzókat!
'''
mgh = 'aáeéiíoóöőuúű'
szoveg = input('Kérem adjon meg egy szöveget: ')
maganhangzo = 0
for k in szoveg:
    if k.lower() in mgh:
        maganhangzo += 1
print(maganhangzo)

'''

# 14. Kérjünk be egy szót és cseréljük le benne a magyar ékezetes betűket az angol ábécé megfelelő ékezet nélküli betűire.
'''
mghs = {,a,: 'a'
         ,á,: 'a'
         ,e,: 'e'
         ,é,: 'e'
         ,i,: 'i'
         ,í,: 'i'
         ,o,: 'o'
         ,ó,: 'o'
         ,ö,: 'o'
         ,ő,: 'o'
         ,u,: 'u'
         ,ú,: 'u'
         ,ű,: 'u'}
szo = input('Kérem adjon meg egy szót: ')
for k in szo:
    if k in mghs:
        print(mghs[k], end='')
    else:
        print(k, end=)



# 15. Olvassunk be egy szöveget, majd írjuk ki szavanként külön sorba! (Cseréljük le a szóközöket sortörésre!)

print(input('Kérem adjon meg egy szót:').replace('', '\n'))

'''
# 16. Kérjünk be egy szót, és rendezzük ábécé sorrendbe a karaktereit!

'''
szo = input('Kérem adjon meg egy szót: ')
print(sorted(szo))
'''
'''
#vagy
lista = []
for k in szo:
    lista.append(k)
lista.sort()
print(lista)
'''

# 17. Kérjen be a felhasználótól két szót, és döntse el, hogy a két szó anagramma-e! Ha azok voltak, írja ki a képernyőre az
# „Anagramma” szót, ha nem, akkor pedig a „Nem anagramma” szöveget!

'''
szo1 = input('Kérem adjon meg egy szót: ')
szo2 = input('Kérem adjon meg egy második szót: ')

if len(szo1) != len(szo2):
    print('Nem anagramma')
else:
    lista1 = sorted(szo1)
    lista2= sorted(szo2)
    anagrammaE = True
    for i in range(0, len(lista1) - 1):
        if lista1[i] != lista2[i]:
            print('Nem anagramma')
            anagrammaE = False
            break
        if anagrammaE:
            print('Anagramma')
'''
# 18. Generáljunk 8 karakteres véletlen-jelszót az alábbi karakterek felhasználásával: abcdefgh1234567890_
'''
import random as r
karakterek = 'abcdefgh1234567890_'
jelszo = ''
for x in range(8):
    jelszo += karakterek[r.randint(0, len(karakterek) - 1)]
print(jelszo)
'''

#19. Kérjük be a felhasználó vezeték- és keresztnevét, majd ajánljunk felhasználónevet a következő szabályok szerint:
#a. a vezetéknév első két betűje + a keresztnév első két betűje
#b. a vezetéknév első két betűje + a keresztnév utolsó két betűje
#c. a vezetéknév első 3 betűje + egy véletlenszerűen választott háromjegyű szám
'''
import random as r
vnev = input('Kérem adja meg vezetéknevét: ')
knev = input('Kérem adja meg keresztnevét: ')
print(f'Ajánlot felh_nev: \n'
      f'\t- {vnev[0:2]}{knev[0:2]}\n'
      f'\t- {vnev[0:2]}{knev[-2:]}\n'
      f'\t- {vnev[0:3]}{r.randint(100, 999)}')
'''


# 20. Kérjünk be egy budapesti postai irányítószámot, majd írjuk ki a megfelelő kerületet
# (az irányítószám középső kétszámjegye)!
'''
irszam = input('Kérem adjon meg egy BP-i irányítószámot:')

print(f' A kerület: {irszam[1:3]}')
'''
'''
print(input('Kérem a BP-i ir számot:')[1:3])
'''
'''
irszam = ''
while not (len(irszam) == 4 and irszam[0] == '1'):
    irszam = input('Kérem a bp-i ir számot: ')
print(f'Az írszam: {irszam[1:3]}.kerület.')
'''




# 21. Készítsünk programot, amellyel a j és ly betűs szavakat gyakorolhatjuk. Egy string tömbbe vegyük fel a gyakorlásra szánt
# szavakat. Írassuk ki a képernyőre a szavakat úgy, hogy a j illetve ly betűk helyére _ kerüljön! (ly esetén is csak egy _ ). A
# felhasználó a billentyűzetről adja meg, hogy j vagy ly a helyes, a program pedig írja ki, hogy jól válaszolt-e. Számoljuk a
# helyes megoldásokat, és a végén írjuk ki az eredményt.
'''
szavak = ["vaj", "kulcslyuk"]
helyesValaszok = 0
for i in range(len(szavak)):
    valasz = input(f"{szavak[i].replace('j', '_').replace('ly', '_')}: ")
    if valasz in szavak[i]:
        helyesValaszok += 1
        print(f'A helyes válaszok száma: {helyesValaszok}')
'''
'''
szavak = ["jaj"]
helyesValaszok = 0
for i in range(len(szavak)):
    betuk = {}
    for j in range(len(szavak[i])):
        if szavak[i][j] == 'j':
            betuk[j] = 'j'

        betuk[szavak.index('ly')] = 'ly'

    print(f"{szavak[i].replace('j', '_').replace('ly', '_')}: ")

    lista = list(betuk.keys())
    lista.sort()
    for j in range(len(lista)):
        valasz = input('Válasz:')
        if valasz in szavak[i]:
            helyesValaszok += 1
            print(f'A helyes válaszok száma: {helyesValaszok}')

'''


# 22. Kérjen be a felhasználótól egy szöveget, majd határozza meg, hogy hány különböző karakter található a szövegben!
# A darabszámot és a karaktereket írja ki a képernyőre!
'''
szoveg = input('kérem adjon meg egy szöveget:')
betuk = {}
for k in szoveg.lower()
    if k in '?, _ '
        continue
    if k not in betuk:
        betuk[k] = 1
    else:
        betuk[k] += 1
print('A szövegben szereplő betűk:')
for x in betuk:
    print(f'\t{x}: {betuk[x]}')

'''

# 23. Kérjünk be egy szót, majd a betűit egymás után felvillantva jelenítsük meg az ablakban!

# from time import sleep
# szo = input('kérem adjon meg egy szót:')
# for k in szo:
#     print(k, end=' ')
#     sleep(.5)


# 24. Készítsünk programot, amely egy megadott szót kiír az ablak felső részére, majd a szó betűit bizonyos időközönként
#egymás után lepotyogtatja az ablak aljára

