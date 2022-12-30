print("Podaj kolejna liczbe, jesli chcesz zakonczyc dodawanie napisz 'stop'")
i = 0
lista = []

while 0 == 0:
    item = input(f"Wprowadz {i + 1}. liczbe: ")
    if item == "stop":
        break
    item = int(item)
    lista.append(item)
    i += 1

print(f"suma {sum(lista)}")
print(f"srednia {sum(lista) / len(lista)}")

if len(lista) % 2 == 0:
    print(f"mediana {((lista[int(len(lista) / 2)] - 1) + (lista[int(len(lista) / 2)] + 1)) / 2}")
else:
    print(f"mediana {lista[int(len(lista) / 2)]}")
