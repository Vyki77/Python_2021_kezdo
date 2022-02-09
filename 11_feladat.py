# Osztályok létrehozása, adattagok, tagfüggvények, konstruktoro

# 1.feladat

class Szemely:

    def __init__(self, nev: str, nem: str, szulev: int, magassag: int ):
        self.nev = nev
        self.nem = nem
        self.szulev = szulev
        self.magassag = magassag

    def kor(self, ev: int) -> int:
        if ev < self.szulev:
            return - 1

        return ev - self.szulev

    def termet(self) -> str:
        if self.nem == 'Férfi':
            if self.magassag <= 165:
                return 'alacsony'
            if 165 < self.magassag < 180:
                return 'átlagos'
            return 'magas'
        else:
            if self.magassag <= 155:
                return 'alacsony'
            if 155 < self.magassag < 170:
                return 'átlagos'
            return 'magas'
    def osszeillo(self):

