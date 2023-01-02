i = 0
for gender in ["Mezczyzna", "Kobieta"]:
    for color in ["bialy", "czarny", "zielony", "czerwony", "niebieski"]:
        for size in ["XL", "L", "M", "S"]:
            try:
                output = open("wyjsciezadanie97_metka" + str(i) + ".txt", "w")
                output.write(gender + ", " + color + ", " + size)
                i += 1
            except IOError:
                print("Blad otwierania pliku")
                exit()
            finally:
                output.close()
