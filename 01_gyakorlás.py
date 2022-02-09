'''
import math

print('Hello Viki!')
print('hello ' + 'Viki')
print(f'hello Viki' 'baby')
print('hello Viki ' 'cica')
print(44)
print(44 * 3)
print('alma ' * 3)
print('alma * 3')
print('korom: {44}')
print(f'korom: {44}')
print('korom: ' + str(44))
print(20 / 2)
print(20 // 2)
print(20 % 3)
print(20 ** 2)
print(float(20 ** 2))
print(pow(20,2))
print(math.sqrt(25))
print(int(math.sqrt(25)))
print(5 + 5)


if (30 % 2 == 0):
    print('páros')
else:
    print('páratlan')


if (25 % 2 == 0):
    print('páros')
else:
    print('páratlan')


szam = 25
if (int(szam % 2 == 0)):
    print('páros')
else:
    print('páratlan')

'''
'''
homerseklet = 17
if (homerseklet < 15):
    print('Hideg van')
elif (homerseklet > 15):
    print('Meleg van')
else:
    print('Kellemes az idő')
'''
'''
korom = 46
if (korom < 46):
    print('éretlen')
elif(korom > 46):
    print('tata')
else:
    print('szexi')


fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")


birth_year = int(input('Enter your birth year:'))
age = 2022 - birth_year
print(age)


firtht = input('Firtht number:')
second = input('Second number:')
sum = firtht + second
print(sum)           # run: 1020 egymás után kiírja a két számot


firtht = int(input('Firtht number:'))
second = int(input('Second number:'))
sum = firtht + second
print(sum)           # run: 30, összeadja, mert int-be konvertáltam


firtht = float(input('Firtht number:'))
second = float(input('Second number:'))
sum = firtht + second
print('Sum:' + str(sum))   # run: 30.1

'''

# age = 77
# szoveg = 'Python for Beginners. {}'
#
# print(szoveg)                   # run: Python for Beginners. - kiírja
# print(szoveg.upper())           # run: PYTHON FOR BEGINNERS. - nagybetűssé alakítja
# print(szoveg.lower())           # run: python for beginners. - kisbetűssé alakítja
# print(szoveg.split())           # run: ['Python', 'for', 'Beginners.'] -
# print(szoveg.strip())           # run:  Python for Beginners. -
# print(szoveg.find('f'))         # run: 7, a hetedik betű, 0-tól a szóközöket is számolja
# print(szoveg.index('f'))        # run: 7, a hetedik betű, 0-tól a szóközöket is számolja
# print(szoveg.replace('for','4'))  # run: Python 4 Beginners. - kicseráli a megadott szöveget
# print(szoveg.count('n'))        # run: 3, megszámolja az 'n' betűt
# print(szoveg.endswith('.'))     # run: True, megvizsgálja a megadott végződés egyezik-e. Igaz vagy Hamis -t ad vissza
# print(szoveg.capitalize())      # run: az első betűt nagybetűre módosítja
# print(szoveg.casefold())        # run: kis és nagybetűk nélküli szöveg összehasonlítás
# print(szoveg.format(age))        # run: a {} -be az age változó értéke kerül a stringbe
#


# WHILE LOOP
'''
i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i <= 15:
    print(i * '*')
    i += 1 
'''

# LISTÁK

# lista = ['Viki', 'Zsolt', 'Gábor','Petra', 'Antónia', 'Zsozsó']
# lista[1] = 'Zsoli'
# print(min(lista))
# print(lista)
# print(lista[:-1])
# print(lista[-1])
# print(max(lista))


# FOR, WHILE LOOP
'''
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lista:
    print(i)            # kiírja 0-tól 9-ig
i = 0
while i < len(lista):                           # a for és while ciklussal is ki tudom íni úgyan azt
    print(lista[i])    # kiírja 0-tól 9-ig
    i += 1
'''
'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
'''
'''
numbers = range(20,100,2)
for number in numbers:
    print(number)
'''
# DICTIONARY - SZÓTÁR
'''
car ={"brand": "Ford","model": "Mustang","year": 1964}
print(car.get("model"))              # run: Mustang
'''
'''
car ={"brand": "Ford","model": "Mustang","year": 1964}

car["year"] = 2020              # kicseréli a "year" értékét
car.pop("model")                # eltávolítja a "model" elemet
car.clear()                     # törli az egész szótárt
'''

# 1. lekissebb közös többszörös. # a nagyobb szám többszöröseit vesszük és elosztjuk a kissebb számmal, amig a maradék 0
'''
szam1 = int(input('Kérem az első számot:'))
szam2 = int(input('Kérem a második számot:'))

if szam1 > szam2:
    nagyobb = szam1
    kissebb = szam2
else:
    nagyobb = szam2
    kissebb = szam1

kell = 1
x = 0
while kell == 1:
    x += 1
    tobbszoros = nagyobb * x
    if tobbszoros % kissebb == 0:
        kell = 0
        print(f'Legkissebb közös többszörös:  {tobbszoros}')
'''

# 2. két szám átlag számítása, fügvény segítségével
'''
def atlag(a,b):
    szamitas = (a+b)/2
    return szamitas

szam1 = int(input('Kérem az első számot:'))
szam2 = int(input('Kérem a második számot:'))

print(f'A két szám átlaga: ', atlag(szam1, szam2))
'''

