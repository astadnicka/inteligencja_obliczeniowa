import math
from datetime import datetime

# Funkcja obliczająca biorytmy
def oblicz_biorytmy(dzien_zycia):
    # Wzory biorytmów
    fizyczny = math.sin((2 * math.pi / 23) * dzien_zycia)
    emocjonalny = math.sin((2 * math.pi / 28) * dzien_zycia)
    intelektualny = math.sin((2 * math.pi / 33) * dzien_zycia)
    return fizyczny, emocjonalny, intelektualny

# Funkcja obliczająca dzień życia na podstawie daty urodzenia
def oblicz_dzien_zycia(rok, miesiac, dzien):
    data_urodzenia = datetime(rok, miesiac, dzien)
    dzisiaj = datetime.today()
    roznica = dzisiaj - data_urodzenia
    return roznica.days

# Funkcja główna
def biorytmy():
    # Pobieranie danych od użytkownika
    imie = input("Podaj swoje imię: ")
    rok = int(input("Podaj rok urodzenia: "))
    miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
    dzien = int(input("Podaj dzień urodzenia (1-31): "))

    # Obliczanie dnia życia
    dzien_zycia = oblicz_dzien_zycia(rok, miesiac, dzien)

    # Obliczanie biorytmów
    fizyczny, emocjonalny, intelektualny = oblicz_biorytmy(dzien_zycia)

    # Wyświetlanie wyników
    print(f"\nCześć {imie}!")
    print(f"Dzień twojego życia: {dzien_zycia}")
    print(f"Twoje wyniki biorytmów dzisiaj:")
    print(f"Fizyczny: {fizyczny:.4f}")
    print(f"Emocjonalny: {emocjonalny:.4f}")
    print(f"Intelektualny: {intelektualny:.4f}")

    # Interpretacja wyników
    for wynik, nazwa in zip([fizyczny, emocjonalny, intelektualny],
                            ["Fizyczny", "Emocjonalny", "Intelektualny"]):
        if wynik > 0.5:
            print(f"{nazwa}: Świetnie! Czujesz się na topie!")
        elif wynik < -0.5:
            print(f"{nazwa}: To może być trudny dzień. Nie martw się!")
            # Sprawdzanie prognozy na następny dzień
            nastepny_dzien_zycia = dzien_zycia + 1
            nastepny_wynik = math.sin((2 * math.pi / (23 if nazwa == "Fizyczny" else (28 if nazwa == "Emocjonalny" else 33))) * nastepny_dzien_zycia)
            if nastepny_wynik > wynik:
                print("Nie martw się. Jutro będzie lepiej!")
        else:
            print(f"{nazwa}: Czasami bywa średnio, ale nie ma się czym martwić!")

# Uruchomienie programu
biorytmy()
