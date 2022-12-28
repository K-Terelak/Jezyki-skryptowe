alfabet = input("Podaj ciag liter: ")

samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y']
for letter in alfabet:
    if letter in samogloski:
        print(letter)
