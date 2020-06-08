a = [1, 3, 33, 0, 3, 32, 8, 3]

for i in range(0, len(a)):
    for j in range(i +1, len(a)):
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(a)