import random

list1 = []
for i in range(0, 20):
    m = int(input("enter number:"))
    list1.append(m)

print(list1)

for i in range(0, 20):
    list1[i] = list1[i] * list1[i]
print(list1)
print("Max: ", max(list1))
print("Min: ", min(list1))
