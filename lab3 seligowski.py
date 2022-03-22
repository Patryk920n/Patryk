import sys
import math
import random

# zad 1
a = [1-x for x in range(1,11)]
print(a)
b = [4**x for x in range(8)]
print(b)
c = [x for x in b if x%2==0]
print(c)

# zad 2
list = []
for x in range(10):
    list.append(random.randint(1,100))
print(list)
list2 = [x for x in list if x%2==0]
print(list2)

# zad 3
slownik = {"lizak":"szt","mąka":"kg","mleko":"litr"}
print(slownik)
slownik2 = [x for x in slownik.values() if x == "szt"]
print(slownik2)

# zad 4
def trojkat(a,b,c):
    if a**2+b**2==c**2:
        return 1
    else:
        return -1
print(trojkat(3,4,5))

# zad 5
def trapez(a=1,b=1,h=1):
    wynik=((a+b)*h)/2
    return wynik
print(trapez())
print(trapez(5,5,2))

# zad 7
def il_el_ciagu7 (* liczby) :
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for x in liczby:
            iloczyn *= x
        return iloczyn

print(il_el_ciagu7(1,2,3,4))

# zad 8
def licz(**slownik):
    print(sum(slownik.values()))
licz(lizak=3.5,mąka=1.5,mleko=2)
