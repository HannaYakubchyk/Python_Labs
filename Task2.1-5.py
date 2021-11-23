import random

size = int(input("Введите размер списка: "))

A = []
for i in range(size):
    a = random.randint(0, 100)
    A.append(a)

print("Введены значения: "+str(A))


minimum = A[0]
for i in range(len(A)):
    if A[i] % 2 == 0 and A[i] < minimum:
        minimum = A[i]

print("Наименьший четный элемент списка или первый элемент (нечетный): "+str(minimum))

Sorted_A = sorted(A)
print("Отсортированный список: "+str(Sorted_A))
