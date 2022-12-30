lista = []

with open('in82.txt') as plik:
    lines = plik.read().splitlines()
    for line in lines:
        lista.append(int(line))

print(f"suma {sum(lista)}")
print(f"srednia {sum(lista) / len(lista)}")

if len(lista) % 2 == 0:
    print(f"mediana {((lista[int(len(lista) / 2)] - 1) + (lista[int(len(lista) / 2)] + 1)) / 2}")
else:
    print(f"mediana {lista[int(len(lista) / 2)]}")