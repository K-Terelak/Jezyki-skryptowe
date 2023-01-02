
import calendar

a = input("Podaj rok od ktorego chcesz rozpoczac sprawdzanie: ")
try:
    a = int(a)
except ValueError:
    print("Podales zla wartosc")
    exit()

b = input("Podaj rok na ktorych chcesz zakonczyc sprawdzanie: ")
try:
    b = int(b)
except ValueError:
    print("Podales zla wartosc")
    exit()

for year in range(min(a, b), max(a, b)):
    if calendar.isleap(year):
        print("Rok " + str(year) + " jest przestepny.")