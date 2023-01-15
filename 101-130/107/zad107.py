def encrypt(text, s):
    result = ""
    for char in text:

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print(f"Text: {text} ->  {result}")


def decrypt(text, s):
    result = ""
    for char in text:

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    print(f"Text: {text} ->  {result}")


encrypt("AZaz", 2)
decrypt("CBcb", 2)
