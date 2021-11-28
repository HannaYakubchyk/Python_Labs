# В матрице найти номер строки, сумма чисел в которой максимальна.

import numpy as np

rows = int(input("Введите количество строк матрицы: "))
columns = int(input("Введите количество столбцов матрицы: "))
a = np.random.randint(1, 100, (rows, columns)) # случайный массив со значениями от 1 до 100
print("Матрица заполнена следующими случайными значениями: \n", a)
print("Сумма значений каждой строки", a.sum(axis=1))
print("Индекс строки, сумма чисел в которой максимальна", a.sum(axis=1).argmax())
