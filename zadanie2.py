a1,b1,c1 = 10,5,2
a2,b2,c2 = 4,6,8

W = a1 * b2 - a2 * b1
Wx = c1 * b2 - c2 * b1
Wy = a1 * c2 - a2 * c1

print(f"Wyznacznik główny W = {W}")
print(f"Wyznacznik Wx = {Wx}")
print(f"Wyznacznik Wy = {Wy}\n")


if W != 0:
    x = Wx / W
    y = Wy / W
    print("Wynik: Układ jest OZNACZONY (posiada jedno rozwiązanie).")
    print(f"x = {x}")
    print(f"y = {y}")

    print("\n--- SPRAWDZENIE ---")
    lewa1 = a1 * x + b1 * y
    lewa2 = a2 * x + b2 * y
    print(f"Równanie 1: {a1}*({x}) + {b1}*({y}) = {lewa1} (Oczekiwano: {c1})")
    print(f"Równanie 2: {a2}*({x}) + {b2}*({y}) = {lewa2} (Oczekiwano: {c2})")

elif W == 0 and (Wx != 0 or Wy != 0):
    print("Wynik: Układ jest SPRZECZNY (brak rozwiązań).")

else:
    print("Wynik: Układ jest NIEOZNACZONY (nieskończenie wiele rozwiązań).")