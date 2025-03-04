import numpy as np
import matplotlib.pyplot as plt
import random

g = 9.81
v0 = 50
h = 100


def oblicz_odleglosc(alpha):
    theta = np.radians(alpha)
    return (v0 * np.sin(theta) + np.sqrt(v0 ** 2 * np.sin(theta) ** 2 + 2 * g * h)) * v0 * np.cos(theta) / g


def oblicz_trajectorie(alpha):
    theta = np.radians(alpha)
    t_flight = (v0 * np.sin(theta) + np.sqrt(v0 ** 2 * np.sin(theta) ** 2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, 500)
    return v0 * np.cos(theta) * t, h + v0 * np.sin(theta) * t - 0.5 * g * t ** 2


def rysuj_trajektorie(x, y, target):
    plt.plot(x, y, 'b', label="Trajektoria pocisku")
    plt.axvline(x=target, color='red', linestyle='--', label=f'Cel: {target} m')
    plt.axhline(0, color='black')
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    target = random.randint(50, 340)
    print(f"Cel: {target} m")

    attempts = 0
    while True:
        try:
            alpha = float(input("Podaj kąt strzału: "))
            distance = oblicz_odleglosc(alpha)
            print(f"Pocisk: {distance:.2f} m")

            if target - 5 <= distance <= target + 5:
                print(f"Cel trafiony! Prób: {attempts + 1}")
                x, y = oblicz_trajectorie(alpha)
                rysuj_trajektorie(x, y, target)
                break
            else:
                print("Chybiony! Spróbuj ponownie.")
        except ValueError:
            print("Niepoprawny kąt!")

        attempts += 1


if __name__ == "__main__":
    main()
