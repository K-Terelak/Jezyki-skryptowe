with open("danezadanie91.txt", "r") as tekst:
    d = {}
    lines = tekst.readlines()
    for line in lines:
        for i in line.strip():
            if i.isalnum():
                d[i] = d.get(i, 0) + 1
    print(d)
