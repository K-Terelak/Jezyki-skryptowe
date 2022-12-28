print("Podaj kolejne elementy listy, jesli chcesz zakonczyc dodawanie elementów do listy napisz 'stop'")
i = 0
lista = []

while 0 == 0:
    item = input(f"Wprowadz {i + 1}. element listy: ")
    if item == "stop":
        break
    lista.append(item)
    i += 1

print("\nElementy listy: ")
for item in lista:
    print(item)
