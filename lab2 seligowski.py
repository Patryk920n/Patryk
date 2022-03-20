import sys
import math
# zad 1
lista = ["Pilka nozna", "tenis ziemny", "Biegi"]
lista.reverse()
lista.append("koszykowka")
lista.append("tenis stolowy")
print(lista)

# zad 2
slownik = {"itd":"i tak dalej", "dr":"doktor", "nr":"numer"}
print(slownik.keys())

# zad 3
gry={"fps":"Hunt: Showdown","rpg":"Divinity Original Sin 2","strategy":"Warhammer 2"}
licznik = 0
for x in gry:
    print(x)
    licznik+=1
print("Liczba gier: ",licznik)

# zad 4
zdanie = input("Podaj zdanie: ")
zdanie = str(zdanie)
list = []
licznik = 0
list.extend(zdanie)
for x in list:
    if x == "a":
        licznik+=1
print("a wystapilo ",licznik," razy")

# zad 5
wynik=0
a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")
c = input("Podaj liczbe c: ")
a = int(a)
b = int(b)
c = int(c)
wynik=a**b+c
print("wynik: ",wynik)

# zad 6
d = input("Podaj liczbe d: ")
e = input("Podaj liczbe e: ")
f = input("Podaj liczbe f: ")
d = int(d)
e = int(e)
f = int(f)
wynik=0
if d > e:
    if d > f:
        print("liczba ",d," jest najwieksza")
    else:
        print("liczba ", f, " jest najwieksza")
elif e > f:
    print("liczba ", e, " jest najwieksza")
else:
    print("liczba ", f, " jest najwieksza")

# zad 7

# liczby = [5,3,float(12),float(5)]
# for x in liczby:
#
# print(liczby)

#zad 8
z=0
parzyste=[]
while z != 10:
    l = input("Podaj liczbe l: ")
    l = int(l)
    if l%2==0:
        parzyste.append(l)
    z+=1
print(parzyste)


# zad 9
p = input("Podaj liczbe: ")
p = int(p)
if p >= 0:
    print(math.sqrt(p))
else:
    print("Padales wartosc ujemna pajacu")