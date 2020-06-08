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