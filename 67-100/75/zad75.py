def compareLists(a, b):
    size = max(len(a), len(b))
    for i in range(0, size):
        if i < min(len(a), len(b)):
            if a[i] == b[i]:
                print(f"{a[i]} == {b[i]}")
            else:
                print(f"{a[i]} =/= {b[i]}")
        else:
            print(f"Nie można porównać elementów, ponieważ lista {1 if len(a) < len(b) else 2} nie ma tylu elementów")


lst1 = []
lst1.append(1)
lst1.append('b')
lst1.append(None)
lst1.append(0.5)

lst2 = []
lst2.append(1)
lst2.append('b')
lst2.append(None)
lst2.append(0.5)

compareLists(lst1, lst2)
