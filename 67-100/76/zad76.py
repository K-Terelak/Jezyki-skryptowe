def contains(a, b, e):
    if e in a or e in b:
        print(f"element '{e}' należy do jednej z podanych list")
    else:
        print(f"element '{e}' nie należy do jednej z podanych list")


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

contains(lst1, lst2, 'b')
