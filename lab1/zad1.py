import datetime
import math

imie = input('Podaj imię: ')
rok = int(input('Podaj rok urodzenia: '))
miesiac = int(input('Podaj miesiąc urodzenia: '))
dzien = int(input('Podaj dzień urodzenia: '))

data_urodzenia = datetime.date(rok, miesiac, dzien)
dzis = datetime.date.today()
t = (dzis - data_urodzenia).days


print('Siema ', imie)
print('Jesteś na ziemii już ', t, "dni")

yp = math.sin(2 * math.pi * t / 23)
ye = math.sin(2 * math.pi * t / 28)
yi = math.sin(2 * math.pi * t / 33)

yp_tomorrow = math.sin(2 * math.pi * (t + 1) / 23)
ye_tomorrow = math.sin(2 * math.pi * (t + 1) / 28)
yi_tomorrow = math.sin(2 * math.pi * (t + 1) / 33)


print(f"Twój biorytm na dziś:")
print(f"Fizyczny: {yp:.2f}")
print(f"Emocjonalny: {ye:.2f}")
print(f"Intelektualny: {yi:.2f}")

print("\nInterpretacja wyników:")

if yp > 0.5:
    print("Fizyczny: Wysoki poziom! Gratulacje, to dobry dzień! 🎉")
elif yp < -0.5:
    print("Fizyczny: Niski poziom. Może być ciężej. 😞", end=" ")
    if yp_tomorrow > yp:
        print("Nie martw się. Jutro będzie lepiej! 😊")
    else:
        print("Jutro może być tylko gorzej")

if ye > 0.5:
    print("Emocjonalny: Przepełniają cię dziś pozytywne emocje! 😃")
elif ye < -0.5:
    print("Emocjonalny: Niski poziom. Możesz czuć się gorzej. 😞", end=" ")
    if ye_tomorrow > ye:
        print("Nie martw się. Jutro będzie lepiej! 😊")
    else:
        print("Jutro może być tylko gorzej")

if yi > 0.5:
    print("Intelektualny: Ależ ty dziś mądra! 🧠✨")
elif yi < -0.5:
    print("Intelektualny: Głupia jesteś dziś. 🤯", end=" ")
    if yi_tomorrow > yi:
        print("Nie martw się. Jutro będzie lepiej! 😊")
    else:
        print("Jutro może być tylko gorzej")

if -0.5 <= yp <= 0.5:
    print("Fizyczny: Średni poziom. Neutralny dzień. 😐")
if -0.5 <= ye <= 0.5:
    print("Emocjonalny: Średni poziom. Neutralny dzień. 😐")
if -0.5 <= yi <= 0.5:
    print("Intelektualny: Średni poziom. Neutralny dzień. 😐")


#20min
