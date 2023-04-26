import math

x = int(input())
x1 = math.ceil(math.pow(x, 5/3) + math.tan(math.radians(x)))
x2 = math.floor(math.pow(math.pi, 2 + math.atan(math.pow(math.sin(math.radians(x)), 2))))
print(math.gcd(x1, x2))
