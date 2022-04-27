print('Hihihi')
# says hi to a guy

def plus(a,b):
    return a+b


print(plus(10,10))

from math import sqrt


def solve(a, b, c):
    d = sqrt(b ** 2 - 4 * a * c)

    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)

    return x1, x2


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)