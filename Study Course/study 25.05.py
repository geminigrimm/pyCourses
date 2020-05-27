a = 'hello'
b = 'World'

print (a+ "," + b)

print(a[0]) # отображаем первый элемент строки( индекс 0)

print(a[1:3]) # отображаем второй-третий элементы строки ( индекс 1,2 , последнее значение не берется!!!)

len(a) # определение длины строки


firstname = 'Дмитрий'
lastname = 'Иванов'
age = 35

print("Hi, my name is ", firstname," " ,lastname,", I am " , str(age) , " years old") # выводим текст с вложенными переменными

t = firstname[0] + firstname[2] + firstname[4]  # выводим строку только с четными элементами строки
print(t)


# добавление значений в начало и конец списка
data = [1,2,3]
data.append('4') # в конец
print(data)
data.insert(0,0) # в начало по индексу
print(data)

# объединение двух список
data = [1,2,3]
data1 = [4,5,6]
data.extend(data1)
print(data)

# объединение двух список путем сложение
data1 = [1,2,3]
data2 = [4,5,6]

data = data1 + data2
print(data)


# удаление значения по индексу

data = [1,3,"a"]
del data[2]
print(data)

# поиск количества повторений
data = [1,2,3,3,4,3,3]
count = 0

for i in data:
    if i == 3:
        count+=1
print(count)


# объединение и добавление значений

data = [1,2,3]
data1 = [4,5,6]

data.append('4')
data.insert(0,0)
data1.append('7')
data1.insert(0,3)
print(data)
print(data1)

data.extend(data1)
print(data)


# преобразование списка в кортеж
data = {1,2,3,3}
result = tuple(data)
print(result)


#множество
data = {1,2,3,3}
print(data)
result = set(data)
print (result)

#словарь - получить все ключ-значение
# pprint - для удобного визульного отражения списка
import pprint
data = {'firstname':'ivan','lastname':'durovich','age':'32', 'list': [1,2,3],'set':{1,2,3,4}, 'dict':{"one":"1"}}

print(data.keys())  # возвращаем все ключи
print(data.values())  # возвращаем все значения
print(data.items()) # возвращаем все пары ключ-значение для словаря в строку

for key, value in data.items(): # возвращаем все пары ключ-значение для словаря в столбик
    print(key,value)


data1 = [4,2,3]  # список
data2 = tuple(data1) # список преобразуем в кортеж
data1.sort()  # сортировка для списка
data2.sort()    # сортировка для кортежа
print(data1)   # сортировка сработала
print(data2)   # сортировка не сработала, т.к кортеж упорядочен и не поддерживает сортировку

# Проверка, читается ли строка слева-направо и справа-налево одинаково
data = "wowф"
print(data[::-1])
if data [::-1] == data:
    print(True)
else:
    print("Не читается")


# сложить возрасты саши и маши
data = "sasha j4la3, masha 23"

age = ''
for i in data:
        if i.isdigit(): # если элемент в строке цифра, тогда добавлем его в age.
            age += i
print(age)

sasha = int(age[0:2])
masha = int(age[2:4])

print(sasha+masha)





