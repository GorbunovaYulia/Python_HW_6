"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
"""
def fill_array(array_size):
    array = []
    for i in range(array_size):
        num = int(input("Введите элемент массива: "))
        array.append(num)
    return array

def find_unique(array1, array2):
    for i in range(array_size1):
        if array1[i] not in array2:
            print(array1[i], end = " ")

array_size1 = int(input("Введите количество элементов в первом массиве: "))
array1 = fill_array(array_size1)
print(array1)
array_size2 = int(input("Введите количество элементов во втором массиве: "))
array2 = fill_array(array_size2)
print(array2)
find_unique(array1, array2)
