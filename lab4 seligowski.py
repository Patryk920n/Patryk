import sys
import math

#zad1
list = []
for x in range(0,31):
    list.append(x*2)

plik = open('plik.txt', 'a+')
plik.write(str(list))
plik.close()

#zad2
with open('plik.txt', 'r') as plik:
    for linia in plik:
        print(linia)

#zad3
dane = sys.stdin.readline()
plik = open('dane.txt', 'w+', encoding='utf-8')
plik.write(dane)
plik.close()
with open('dane.txt', 'r') as plik:
    for linia in plik:
        print(linia)

#zad4
class Zakupy:
    def __init__(self, nazwa_produktu, ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed  = cena_jed
    def wyświetl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
        return self.ilosc,self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed



start = Zakupy("mąka",2,"kg",1.5)
print("Produkt to: " + start.wyświetl_produkt())
print(start.ile_produktu())
print(str(int(start.ile_kosztuje())) + " złotych")