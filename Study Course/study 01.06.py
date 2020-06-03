a = 1
b = 2
a, b = b, a # обменяться значениями переменных


# присвоение значения переменной
spam, ham = 'yum', 'YUO'
print(spam)

spam = ham = 'lunch'
print(spam)
print(ham)

spams = spams + 42
print(spams)

#отображение строки по стандарту питона
fname = 'Ivan'
lname = 'Petrov'
string_d = f'Hello,{fname} {lname} !'
print(string_d)

# сложение двух чисел с присвоением формата
a = int(input("insert first cell: "))
b = int(input("insert second cell: "))

x = a+b
print(x)

# написать строку в формате {Hello, my name is Alex}
string = 'Hello,_my_name_is_Alex'
string_list = string.split('_')
print(string_list)
result = ' '.join(string_list)
print(result)

# заменить в строке букву
string = 'ping pong'
res_string = string.replace('p','k')
print(res_string)

#поменять местами и добавить !знак в начало и в конец
x = 'hello world'.split()[::-1] # делим на два значения и переворачиваем местами
print(x)
new_x = " ".join(x)
print(new_x)
print(f"! {new_x} !")


print(f"! {' '.join('Hello world'.split()[::-1])} !") #одной строкой инфу выше

#Вывести, если длина строки делится на три без остатка, то добавить !знак в конце
x = input()

if len(x) % 3 == 0:
    print(x,"!")
else:
    print('blank string')

# Проверить, есть ли слово 'code' в строке х
x = 'well done code'.split() #разбиваем на список
if 'code' in x:
    print('Yes')
else:
    print('No')

# в зависимости от х выводить опред слова
x = int(input())

if x < 0:
    print('Wrong input')
elif x < 18:
    print('CocaCola')
else:
    print('Beer')

# в зависимости от длины строки выводить текст
x = str(input())
if len(x) > 5:
    print(x)
elif len(x) < 5:
    print('Need more!')
else:
    print('Its five')

#ctr + /  комментим выделенный код


#ax^2+bx+c = 0  рассчитать квадратное уравнение и сравнить результаты

import math

a = int(input())
b = int(input())
c = int(input())


d = b**2 - 4*a*c


x1 = (-b - math.sqrt(d))/ (2 * a)
x2 = (-b + math.sqrt(d))/ (2 * a)

if x1 != x2:
    print(f" x1:{x1} x2:{x2}")
elif x1 == x2:
    print(f"x1,2 = {x1}")
else:
    print('Not')

# введите рубли и копейки

x = input()
x1 = x.split(".")


if "." not in x:
    print(x,"рублей")
elif "." in x and int(x1[0]) > 0 :
    print(x1[0],"рублей", x1[1],"копеек")
elif int(x1[0]) == 0 and int(x1[1]) > 0:
    print(x1[1],"копеек")
else:
    print('неверный ввод')


# ввести почту и проверить доменое имя
x = input().split("@")
if x[1] == "gmail.com":
    print('@'.join(x))
else:
    print('wrong domain')

# регион_названиетакс_4цифры
x = '2 TBX 467ф'
x1 = x.split()
print(x1)
y = ['TAX','TBX','TEX']


if int(x1[0]) in range(1,8) and x1[1] in y and x1[2].isdigit():
    print('good')
else:
    print('not good')

#решение
tax_list = ["TBX","TAX","TEX"]
string = '7 TBX 000a'
list_number = string.split()
tax_other = ["TBX","TAX"]

try:
    if len(string) == 10:
        if int(list_number[0]) >= 1 and int(list_number[0]) <= 7:
            if int(list_number[0]) == 7 and list_number[1] in tax_list:
                if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                    print('correct')
        elif int(list_number[0]) !=7 and list_number[1] in tax_other:
            if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                print('correct')
except:
    print('error')

# решение 2
tax_list = ["TBX","TAX","TEX"]
string = '7 TBX 0001'
list_number = string.split()
tax_other = ["TBX","TAX"]
if len(string) == 10:
    if int(list_number[0]) >= 0 and int(list_number[0]) <= 7:
        if int(list_number[0]) == 7 and list_number[1] in tax_list:
            if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                print('correct')
            else:
                print('not correct')
    elif int(list_number[0]) != 7 and list_number[1] in tax_other:
        if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
            print('correct')
        else:
            print('not correct')
else:
    print('not correct')




# проверка почты2
string = 'test@viebst-secom.moi.gov.com'
string_list = string.split("@")
for i in string_list[0]:
    if i.isalpha() or i.isdigit() or i in "-_.":
        print(i)
    else:
        print('Error')
        break


for i range(0, len(string_list[1])):
    if i in ignore and i+1 not in ignore
