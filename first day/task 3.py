import math

a = int(input("Введите сторону а "))
b = int(input("Введите сторону b "))
c = int(input("Введите сторону c "))

p = (a+b+c)/2

s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)





