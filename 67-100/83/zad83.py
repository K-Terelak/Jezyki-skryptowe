def pobierz():
    liczba = input("Podaj liczbe calkowita: ")
    try:
        liczba = int(liczba)
        print(f"Podales liczbe calkowita {liczba}")
    except ValueError:
        print("Nie podales liczby calkowitej")


pobierz()
