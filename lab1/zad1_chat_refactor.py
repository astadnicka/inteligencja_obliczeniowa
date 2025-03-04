import datetime
import math

def oblicz_biorytm(dni, cykl):
    return math.sin(2 * math.pi * dni / cykl)

def interpretuj_wynik(wartosc, nazwa):
    if wartosc > 0.5:
        print(f"{nazwa}: Wysoki poziom! To dobry dzień! 🎉")
    elif wartosc < -0.5:
        print(f"{nazwa}: Niski poziom. Może być ciężej. 😞", end=" ")
        print("Jutro będzie lepiej! 😊" if oblicz_biorytm(t + 1, cykle[nazwa]) > wartosc else "Jutro może być tylko gorzej")
    else:
        print(f"{nazwa}: Średni poziom. Neutralny dzień. 😐")

# Pobieranie danych
imie = input("Podaj imię: ")
rok = int(input("Podaj rok urodzenia: "))
miesiac = int(input("Podaj miesiąc urodzenia: "))
dzien = int(input("Podaj dzień urodzenia: "))

data_urodzenia = datetime.date(rok, miesiac, dzien)
t = (datetime.date.today() - data_urodzenia).days

# Obliczanie biorytmów
cykle = {"Fizyczny": 23, "Emocjonalny": 28, "Intelektualny": 33}
biorytmy = {nazwa: oblicz_biorytm(t, cykl) for nazwa, cykl in cykle.items()}

# Wyświetlanie wyników
print(f"\nSiema {imie}! Jesteś na Ziemi już {t} dni.\n")
print("Twój biorytm na dziś:")
for nazwa, wartosc in biorytmy.items():
    print(f"{nazwa}: {wartosc:.2f}")

print("\nInterpretacja wyników:")
for nazwa, wartosc in biorytmy.items():
    interpretuj_wynik(wartosc, nazwa)
