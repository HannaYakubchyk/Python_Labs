#Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку. Подсчитать количество символов в последнем слове F2.

import os

try:
    file1 = open("F1.txt", "r")  #открытие файлв в режиме чтения
    file2 = open("F2.txt", "w") #открытие файлв в режиме записи

    cont = file1.readlines()  #чтение содержимого файла построчно
    for i in range(3, len(cont)): #запись во второй файл только строк, начиная с четвертой
        file2.write(cont[i])

    file2.close() #закрытие файла 2, чтобы далее его открыть в режиме чтения

    file2 = open("F2.txt", "r") #открытие файлв в режиме чтения
    print(file2.read()) #вывод в консоль содержимого 2 файла

    with open('F2.txt') as f:  #поиск последней строки в файле 2
        for line in f:
            pass
        last_line = line
        words = last_line.split() #деление последней строки на слова

    def letters(string):  #функция для счета букв в строке
        count = 0
        for char in string:
            if char.isalpha():
                count += 1
        return count

    print(letters(words[-1])) #вывод в консоль количества символов (вернее букв, так как точка не является частью слова) в последнем слове файла
    print(len(words[-1])) #вывод в консоль количества всех символов в последнем слове (включая знак препинания)

    file1.close()  #закрытие файлов
    file2.close()

except FileNotFoundError:
    print("Not found")
except IOError:
    print("Something else")