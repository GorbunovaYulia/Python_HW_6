"""
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: Ввод:
5 
1 2 3 4 5
Вывод: 0
5
1 5 1 5 1
Вывод: 2
"""
from random import randint

def fill_array(array_size):
   return [randint(1, 10) for i in range(array_size)]
       
array_size = int(input("Введите количество элементов в первом массиве: "))
array = fill_array(array_size)
print(array)

count = 0
for i in range(1, array_size - 1):
   if array[i-1] <  array[i] > array[i+1]:
      count += 1

print(count)