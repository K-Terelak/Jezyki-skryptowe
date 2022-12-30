import random

try:
    with open("in85.txt", "r") as plik:
        fileList = plik.read().splitlines()

except IOError:
    print("Blad otwierania pliku")
    exit()

a = random.randint(1, 100)
b = random.choice(fileList)

try:
    outputFile = open("out85.txt", "w")
    outputFile.writelines(str(a) + "\n")
    outputFile.write(str(b))
    outputFile.close()
except IOError:
    print("Blad otwierania pliku")
    exit()
