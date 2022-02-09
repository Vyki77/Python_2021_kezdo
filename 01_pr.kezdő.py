
# print("Hello World!")

# ami ez utan van , azt a fordito ignoralni fogja

"""
tobbsoros
komment, megjegyzes nekem
"""
'''
tobbsoros
komment ez is
'''
"""VÁLTOZÓK__különböző tárhelyek a memóriában, ami elmenti a változó értékét, később módosítható
nem kezdődhet számmal, csak kis- vagy nagybetűvel, vagy _ al
int szam = 10 (egész szám)
float szam = 3.14 (lebegőpontos, tizedesvessző van benne, pontot használunk)
"""

#szam1 = 10
#szam2 = 20
#szam3 = 2
#szam4 = 5
#szam5 = 4

#print(szam1+szam2-szam3*szam4/szam5)
#szam4 = 8
#print(szam1+szam2-szam3*szam4/szam5)
#szam1 = 3.14
#print(szam1)

# Numbers, String, List, Tuple, Dictionary, user defined, Boolean
# Numbers:
#szam1 = 10 # egész számok (int)
#szam2 = 24.893452 # lebegőpontos(float)
#szam3 = 32.3e18 #  (float)
#szam4 = .876j #komplex számok (complex)

#String:
#nev1 = "Viktória"
#hajszin = 'vörös'
#modas = 'ki korán kell, aranyat lel'

#List:
#lista = []

#Tuple:
#my_tuple = ()

#Dictionary:
#my dict = {}

#Boolean
#igaz = True
#hamis = False

# type kiírja, hogy milyen tipusú
#print(type(hamis)

#Aritmetikai operátorok: +, -, *, /, //, %, **

#szam1 = 5
#szam2 = 13

#print(szam1+szam2)
#print(szam1-szam2)
#print(szam1*szam2)
#print(szam1/szam2)
#print(szam2//szam1)
#print(szam2%szam1)
#print(szam1**szam2)


# Assignment operators - hozzárendelő operátorok: =, +=, -=, *=, /=, //=, %=, **=

#szam = 10
#print(szam)

#szam += 1 # run: a szam most már 11 lesz
#print(szam)

#szam -= 1 # run: a szam 10 lesz
#print(szam)

#szam *= 2 # run: a szam 20 lesz
#print(szam)

#szam /= 3  # run:a szam 6.66666666667 lesz
#print(szam)

#szam //= 2  # run: a szam  3 lesz
#print(szam)

#szam %= 2  # run: szam 1
#print(szam)



                        # LISTS (mutable) - listák (módosítható) objektumok


# 1.módozat

lista1 = []  # létrehoztam a lista1-et, az értékeket később adom hozzá
print(lista1)    # Run: []


lista1.append(100)
lista1.append(101)
lista1.append(102)
lista1.append(103)
lista1.append(104)
print(lista1)     # Run:[100, 101, 102, 103, 104]


lista1.append('Zsolt')
lista1.append('Viki')
lista1.append('Gábor')
print(lista1)      # Run: [100, 101, 102, 103, 104, 'Zsolt', 'Viki', 'Gábor']


lista1[5] = 'Zsoli'
print(lista1)      # Run: [100, 101, 102, 103, 104, 'Zsolt', 'Viki', 'Gábor']  kijavította a Zsoli-ra


lista1.remove('Gábor')
print(lista1)      # Run: [100, 101, 102, 103, 104, 'Zsolt', 'Viki']


# lista1.clear()    # Run: [] törli a listát
# print(lista1)


lista1.insert(5,'Kati')
print(lista1)     # Run: [100, 101, 102, 103, 104, 'Kati', 'Zsolt', 'Viki'] az 5. helyre beszúrja, 0-tól számol


lista1.reverse()
print(lista1)  # Run: ['Viki', 'Zsolt', 'Kati', 104, 103, 102, 101, 100] megfordítja a listát

# 2. módozat

lista2 = [15, 8, 67, 234, 176, 23 ]
lista2.sort()
print(lista2)  # Run: [8, 15, 23, 67, 176, 234]  sorbarakja, keverni az 'int' és 'str' nem lehet



lista3 = ['Ani', 'Vica', 'Gabi', 'Lili']
lista3.sort()
print(lista3)  # Run: ['Ani', 'Gabi', 'Lili', 'Vica']



ABC = ['M', 'L', 'G', 'F', 'E', 'Ő', 'Z', 'A', 'V', 'Á', 'K']
ABC.sort()
print(ABC)   # Run: ['A', 'E', 'F', 'G', 'K', 'L', 'M', 'V', 'Z', 'Á', 'Ő'] sorbarakta, ékezeteket nem értelmezi
print(len(ABC))  # Run: 11,   a lista hossza, megszámolja az ABC betűit
print(max(ABC))  # Run: Ő, a lista utolsó adata
print(min(ABC))  # run: A, a lista első adata



lista4 = ['Viki', 'Zsolt', 'Gábor','Petra', 'Antónia', 'Zsozsó']
print(lista4)    # run: ['Viki', 'Zsolt', 'Gábor', 'Petra', 'Antónia', 'Zsozsó']



                             # Indexelés:

print(lista4[3])  # run: Petra, Indexelés,  kiírja a 3. adatot, 0-tól számolunk
print(lista4[-1])  # run: Zsozsó, Indexelés, kiírja az utolsó adatot
print(lista4[:-1])  # run: ['Viki', 'Zsolt', 'Gábor', 'Petra', 'Antónia']  az utolsóig kiírja, a -1-et már nem

                          # Szeletelés:

print(lista4[0:2])  # run: ['Viki', 'Zsolt'], 0-2-ig kiírja, a 2-est már nem
print(lista4[2:])   # run: ['Gábor', 'Petra', 'Antónia', 'Zsozsó'],  2-től kiírja végig, 2-est is

                            # Listák a listában:

lista5 = [[1,2,3], [4,5,6], [7,8,9]]
print(lista5)  # run: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], listán belüli listák

print(lista5[1])  # run: [4, 5, 6], indexelek
print(lista5[2][1])  # run: 8 , 2.listából az 1 adat

# 3. módozat

tartomany = range(100)
print(tartomany)    #: run: range(0, 100)
print(list(tartomany))   # run: [0, 1, 2, 3, 4, 5, 6, 7, 8,.....97, 98, 99]
print(list(tartomany) + 1)   # run: [0, 1, 2, 3, 4, 5, 6, 7, 8,.....97, 98, 99, 100]



                                # CIKLUSOK:


                  # 1.for loop - for ciklus

for i in range(10):  # i, mint iterátor
   print('Hello')  # run: 10-szer kiírja egymás alá a Hello-t, a print előtt sor behúzás van, 
                                              # ez jelzi, hogy a for loop alá tartozik
   print('Bello')


for i in range(10):
    print(i)        # run: 0-9-ig kiírja a számokat egymás alá
tartomany = range(10)
print(tartomany)      # run: range(0, 10)
print(list(tartomany))  # run: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for x in range(6):
  print("Bármi")      # run: 6 x kiírja "Bármi"



lista1 = ['Viki', 'Zsolt', 'Gabi', 'Petra', 'Lili']
print(lista1)               # run: ['Viki', 'Zsolt', 'Gabi', 'Petra', 'Lili']
print(len(lista1))          # run: 5
for i in range(len(lista1)):
    print(lista1[i])        # run: kiírta a neveket egymás alá


for i in lista1:
    print(i)     # run: kiírta a neveket egymás alá
    
  
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    continue
  print(x)



# 2. while loop - while ciklus


szam = 0

while szam <= 5:
    print('Viki')  # run: végtelenségig kiírja, mert a szam értéke mindig kissebb mint 5
    szam += 2      # run: addig írja ki, amig szam <= 5-el, 3-szor írta ki



# 3. if  elágazások, kondicionálisok - statements, conditionals


if True:
    print('igaz')  # run: igaz
if False:
    print('hamis')  # run: nem ír ki semmit, mert Faslse


kor = 20
if kor < 18:
    print('Se cigi, se pia!')  # run: False, nem írja ki, mert kor > 18

kor = 14
if kor < 18:
    print('Se cigi, se pia!')  # run: Se cigi, se pia!

kor = 18
if kor < 18:
    print('Se cigi, se pia!')  # run: False, nem írja ki, mert kor = 18, nem kissebb

kor = 25
if kor < 18:
    print('Se cigi, se pia!')  # run: False, nem írja ki
elif kor >= 18 and kor < 30:
    print('Jó bulizást!')   # run: Jó bulizást!

kor = 31
if kor < 18:
    print('Se cigi, se pia!')  # run: False, nem írja ki
elif kor >= 18 and kor < 30:
    print('Jó bulizást!')    # run: False, nem írja ki
elif kor > 30 and kor < 65:
    print('Család !')       # run: Család !,  True


kor = 72
if kor < 18:
    print('Se cigi, se pia!') # run:False, nem írja ki
elif kor >= 18 and kor < 30:
    print('Jó bulizást!')    # run: False, nem írja ki
elif kor > 30 and kor < 65:
    print('Család !')       # run: False, nem írja ki   - bármennyi elif-et megadhatok
else:
    print('Unokák!')        # run: Unokák!  , True    -  else csak egyszer lehet

kor = 17
if kor < 18:
    print('Se cigi, se pia!')  # run: Se cigi, se pia!
    if kor > 16:
        print(' Egy kis sör belefér')   # run: Egy kis sör belefér, True
elif kor >= 18 and kor < 30:
    print('Jó bulizást!')
elif kor > 30 and kor < 65:
    print('Család !')
else:
    print('Unokák!')
    
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")    



# FÜGVÉNYEK - def my_function():

# 1.


x = "awesome"

def valami():
  x = "fantastic"             # ha a változót a fügvényen belül hozom létre, akkor csak ott használhatom
  print("Python is " + x)     # run: Python is fantastic

valami()

print("Python is " + x)       # run: Python is awesome, a fügvényen belüli változót kívül nem hasznája

# 2.

def valami():
  global x                    # globális kulcsszót használva, a változó globális hatókörbe tartozik
  x = "fantastic"

valami()

print("Python is " + x)       # run: Python is fantastic

# 3.

x = "awesome"

def valami():
  global x
  x = "fantastic"              # a global parancsal megváltoztatjuk a fügvényen kívüli változó értékét

valami()

print("Python is " + x)       # run: Python is fantastic

# 4.

nevek1 = ['Viki', 'Zsolt', 'Gabi', 'Petra', 'Lili',10]
nevek2 = ['Joli', True, 'Tibi', 'Zoli', 'Brigi', 'Pali']

def nev_print(nev_lista):
    for nev in nev_lista:
      if isinstance(nev, str):         # ha int vagy bool formátumu, akkor is lefut
        print(nev.upper())             # run: kiírja a nevek1 és 2-őt egymás alá nagy betűvel
      else:
        print('nem str típusú, hanem:' + str(type(nev)))

nev_print(nevek1)           # meghívom a fügvényt
nev_print(nevek2)

# 5.

a = 10
b = 20

def osszeadas1():
    print(a + b)
osszeadas1()


def osszeadas2(a, b, c= 2):
    return a + b + c
osszeg = osszeadas2(45, 25)
print(osszeg)
print(osszeadas2(45, 25))


def osszeadas3(*args):
    return sum(args)
print(osszeadas3(10,20,30,40,50,60,70,80,90,100))


def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés van:'
    for k in args:
        koszones += k
        koszones += ', '                            # 2 karaktert adtam hozzá (, és szóköz)
    print(koszones[0:len(koszones)-2])              # a "koszones" végéről kivonom a ( , és szóközt)
udvozlesek('szia', 'hello', 'szevasz', 'by')










