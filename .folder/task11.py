# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
num = abs(int(input("Введите длинну списка чисел: ")))
import random
spisok = list()

def random_list(low, high):
    i = 0
    while i < num:
        rnd = random.randint(low,high)
        spisok.append(rnd)
        i+=1
    return spisok
print(random_list(-10,10))

def dif_count(spisok):
    spisok.sort()
    print(spisok)
    count = 0
    for i in range(0, len(spisok)):
        if spisok[i] != spisok[i - 1]:
            count += 1
    return count
print(dif_count(spisok))