"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
def get_user_data(a):
    n = int(input(a))
    return n

def arif_progress(a1, d, n):
    array = []
    for i in range(1, n+1):
        num = a1 + (i - 1)*d
        array.append(num)
    return array     


a1 = get_user_data("Введите начальное число: ")
d = get_user_data("Введите разность в арифметической пргрессии: ")
n = get_user_data("Введите количество элементов: ")
print(arif_progress(a1, d, n))


