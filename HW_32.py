"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
from random import randint

def get_user_data(a):
    n = int(input(a))
    return n

def fill_array(array_size):
   return [randint(1, 10) for i in range(array_size)]

def find_index(array, minimum, maximum):
    for i in range(len(array)):
       if  minimum <  array[i] < maximum:
            print(i + 1, end = " ")

n = get_user_data("Введите количество элементов в массиве: ")
my_array = fill_array(n)
print(my_array)
min_num = get_user_data("Введите значение минимум: ")
max_num = get_user_data("Введите значение максимум: ")

find_index(my_array, min_num, max_num)