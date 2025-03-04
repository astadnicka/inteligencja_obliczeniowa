import numpy as np
import matplotlib.pyplot as plt
import random

g = 9.81
v0 = 50
h = 100

def oblicz_odleglosc(alpha, v0, h, g):

    theta = np.radians(alpha)
    range_equation = (v0 * np.sin(theta) + np.sqrt(v0 ** 2 * np.sin(theta) ** 2 + 2 * g * h)) * (v0 * np.cos(theta)) / g
    return range_equation

def oblicz_trajectorie(alpha, v0, h, g):

    theta = np.radians(alpha)
    t_flight = (v0 * np.sin(theta) + np.sqrt(v0 ** 2 * np.sin(theta) ** 2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, num=500)
    x = v0 * np.cos(theta) * t
    y = h + v0 * np.sin(theta) * t - 0.5 * g * t ** 2
    return x, y

def rysuj_trajektorie(x, y, target):

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'b', label="Trajektoria pocisku")

    plt.axvline(x=target, color='red', linestyle='--', label=f'Cel: {target} m')

    plt.axhline(0, color='black', linewidth=1)  # Ziemia
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.title("Trajektoria pocisku Warwolf")
    plt.legend()
    plt.grid(True)
    plt.savefig("trajektoria.png")
    plt.show()

def main():
    target = random.randint(50, 340)
    print(f"Cel znajduje się w odległości: {target} m.")

    attempts = 0

    while True:
        try:
            alpha = float(input("Podaj kąt strzału w stopniach: "))
        except ValueError:
            print("Proszę podać prawidłowy kąt w stopniach.")
            continue

        distance = oblicz_odleglosc(alpha, v0, h, g)
        print(f"Pocisk uderzył w odległości: {distance:.2f} m.")

        if target - 5 <= distance <= target + 5:
            print(f"Cel trafiony! Liczba prób: {attempts + 1}")

            x, y = oblicz_trajectorie(alpha, v0, h, g)
            rysuj_trajektorie(x, y, target)

            break
        else:
            print("Chybiony! Spróbuj ponownie.")

        attempts += 1

if __name__ == "__main__":
    main()
