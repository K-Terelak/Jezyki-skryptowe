import random


def matrixGen(w, k, dane):
    index = 0
    for y in range(w):
        for x in range(k):
            print(f"{dane[index]}", end=" ")
            index += 1
        print()


wiersze = input("Podaj liczbe wierszy: ")
kolumny = input("Podaj liczbe kolumn: ")

try:
    wiersze = int(wiersze)
except ValueError:
    print("Wiersze musza byc liczba calkowita")
    exit()

try:
    kolumny = int(kolumny)
except ValueError:
    print("Kolumny musza byc liczba calkowita")
    exit()

liczby = []
for x in range(wiersze * kolumny):
    liczby.append(random.randint(0, 9))

matrixGen(wiersze, kolumny, liczby)
