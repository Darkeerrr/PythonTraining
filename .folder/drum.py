# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

import random
new_list = list()
count = abs(int(input("Какой длинны будет массив? ")))
i = 0
while count > i:
    a = abs(int(input("Введите число в список: ")))
    new_list.append(a)
    i+=1
print(new_list)

def move_list(new_list):
    move = int(input("На сколько шагов сдвинуть число? "))
    if move < 0:
        move = abs(move)
        for i in range(move):
            new_list.append(new_list.pop(0))
    else:
        for i in range(move):
            new_list.insert(0 ,new_list.pop())
    return new_list
print(move_list(new_list))