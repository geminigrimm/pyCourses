# пузырьковая сортировка

a = [1, 3, 33, 0, 3, 32, 8, 3]

for i in range(0, len(a)):
    print(i)
    for j in range(i +1, len(a)):
        print(j)
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(a)


# привести вывод к виду  "name : {name} age: {age}"

data = "sasha j4la3, masha 23"

age = ''
for i in data:
        if i.isdigit():
            age += i
print(age)

sasha = int(age[0:2])
masha = int(age[2:4])

data = "sasha j4la3, masha 23"
data1 = data.replace(",","").split(" ")
age = data.isdigit()
print(data1)
print(age)

print("name:",data1[0],"age:",sasha)
print("name:",data1[2],"age:",masha)


# 1.Создать строку равную третьему символу введенной строки.

text = "Hello world!"

print(text[2])

# 2.	Создать строку равную предпоследнему символу введенной строки.
print(text[-2])

# 3.	Создать строку равную первым пяти символам введенной строки.
print(text[:5])

# 4.	Создать строку равную введенной строку без последних двух символов.
print(text[:-2])

# 5.	Создать строку равную всем элементам введенной строки с четными индексами. (считая, что индексация начинается с 0, поэтому символы выводятся 	начиная с первого, индексы 0,2,4,6….).

text = "Hello world!"

for i in range(0,len(text),2):
    print(text[i])
























