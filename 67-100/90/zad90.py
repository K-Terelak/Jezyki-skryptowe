liczba = input("Podaj liczbe: ")
silnia = 1

try:
    liczba = int(liczba)
except ValueError:
    print("Nalezy podac liczbe calkowita")

for i in range(1, liczba + 1):
    silnia = silnia * i

print(f"Silnia liczby {liczba} to {silnia}")
