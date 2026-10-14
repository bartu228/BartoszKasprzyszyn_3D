import cmath

a=2
b=9
c=5

delta = b**2 - 4*a*c
if delta < 0:
    print("delta jest ujemna")
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print(("miejsca zerowe to:", x1, "i", x2))
elif delta == 0:
    print("delta jest równa 0")
    x0 = -b/(2*a)
    print(x0)
else:
    print("delta jest dodatnia")
    x1 = (-b+cmath.sqrt(delta))/(2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print(("miejsca zerowe to:" ,x1 ,"i" ,x2))