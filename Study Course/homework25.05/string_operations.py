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