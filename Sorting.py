import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


# Функция для сортировки пузырьком bubble:
def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


# 2. Функция сортировки вставками insert:
# Цикл 1 – по i от 1 до (len(A)):					# i - текущая позиция при проходе по списку
# 	Действие – сохранение t = A[i]		# A[i] - вставляемый элемент
# 	Действие – новая  переменная j = i 	# j - позиция в отсортированной части списка
# 	Цикл 2 – по j до 0 и A[j-1]  > t:		# j - смещается справа налево, от больших к                       меньшим
# 		То A[j] = A[j-1] 				       # эл-ты отсортированной части, большие вставляемого
# 		И  j -= 1 			       			# уступают место – сдвигаются (копируются) вправо
# 	Иначе – выход из цикла 2		       # j остановится на посл. эл-те, большем вставляемого
# 	Действие – A[j] = t			              ы# вставляемый эл-т ставится на освободившееся место
#                                                                           место

def InsertSort(A):
    # по псевдокоду
    for i in range(1, len(A)):
        t = A[i]
        j = i
        while j > 0 and A[j - 1] > t:
            A[j] = A[j - 1]
            j -= 1
        A[j] = t


# код из инета
# for i in range(1, len(A)):
#     t = A[i]
#     j = i - 1
#     while j >= 0 and t < A[j]:
#         A[j + 1] = A[j]
#         j -= 1
#     A[j + 1] = t


# 3. Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:
# Цикл 1 – по i от 0 до N/2 :				# i - счетчик пар проходов по списку,
# 										# которых в 2 раза меньше, чем в пузырьковой
# 	Цикл 2 – по j от i до N-1-i :			# j - номер позиции при проходе по списку слева направо
# 		Условие – если A[j]>A[j+1] :	# сравнение текущего элемента со следующим
# 			Действие – перестановка местами A[j] и A[j+1]
# 	Цикл 3 – по j от N-2-i до i+1 : 		# j - номер позиции при проходе по списку справа налево
# 		Условие если A[j]<A[j-1] :		# сравнение текущего элемента с предыдущим
# 			Действие – перестановка местами A[j] и A[j-1]

def ShakerSort(A): #с ошибками
    # for i in range(len(A)//2):
    #     for j in range(A[i], len(A)-1-i):
    #         if A[j] > A[j + 1]: #как в бабл эта часть
    #             a = A[j]
    #             A[j] = A[j + 1]
    #             A[j + 1] = a
    #
    #     for j in range(len(A)-2-i, i+1): чтобы идти слева направо нужно шаг указывать отрицательным (как у Насти)
    #         if A[j] < A[j-1]:
    #             a = A[j]
    #             A[j] = A[j - 1]
    #             A[j - 1] = a

    for i in range(len(A) // 2):  # вариант от Насти рабочий
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i + 1, -1):
            if A[j] < A[j - 1]:
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a


# 4. Функция сортировки выбором select:
# Цикл 1 – по i от 0 до N-1 :		# i - счетчик прохода по списку
# 	Действие – объявление переменной m = i;	# m - номер для мин. из неотсортированных
# 	Цикл 2 – по j от i до N :		# j - счетчик позиции при проходе по неотсортированной части
# 		Условие если A[j]<A[m] :	 # сравнение текущего элемента с текущим минимальным
# 			Действие – запоминаем номер обнаруженного нового минимального эл-та m = j
# 	Действие – перестановка местами A[m] и A[i]

def SelectSort(A):
    for i in range(len(A)-1):
        min = i
        for j in range(i, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(
    ["Размер списка", "Время пузырька", "Время вставки", "Время шейкерной", "Время селектом", "Время быстрой"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    B = A.copy()
    C = A.copy()
    D = A.copy()
    E = A.copy()

    print()
    print()
    print()
    print("Случайный неотсортированный список: " + str(A))
    # print(B)
    # print(C)
    # print(D)
    # print(E)

    # BubbleSort(A)
    # print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    print("************СОРТИРУЕМ************")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка списка в " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + " cекунд")
    print("Список, отсортированный пузырьком: " + str(A))

    t3 = datetime.datetime.now()
    InsertSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Сортировка вставками списка в " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + " cекунд")
    print("Список, отсортированный вставками: " + str(B))
    #
    t5 = datetime.datetime.now()
    ShakerSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Шейкерная сортировка списка в " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + " cекунд")
    print("Список, отсортированный шейкером: " + str(C))

    t7 = datetime.datetime.now()
    SelectSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Сортировка выбором списка в " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + " cекунд")
    print("Список, отсортированный выбором: " + str(D))

    t9 = datetime.datetime.now()
    QuickSort(E, 0, len(B) - 1)
    t10 = datetime.datetime.now()
    y5.append((t10 - t9).total_seconds())
    print("Быстрая сортировка списка в " + str(N) + "   заняла   " + str((t10 - t9).total_seconds()) + " cекунд")
    print("Список, отсортированный быстрой: " + str(E))

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()),
         str((t8 - t7).total_seconds()), str((t10 - t9).total_seconds())])
print(table)

plt.plot(x, y1, "#FF0000")  # пузырек red
plt.plot(x, y2, "#00CED1")  # вставка DarkTurquoise
plt.plot(x, y3, "#2F4F4F")  # шейкер grey
plt.plot(x, y4, "#FF8C00")  # селект orange
plt.plot(x, y5, "#0000FF")  # быстрая blue
plt.show()
