# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
num = abs(int(input("Введите число фибаначи: ")))
f_0 = 0
f_1 = 1
f_2 = 1
n = 3
while f_2 < num:
    f_0 = f_1
    f_1 = f_2
    f_2 = f_0 + f_1
    n += 1
    if num == f_2:
        print(n)
    elif num < f_2:
        if abs(num - f_2) == abs(num - f_1):
            print(f"Ближайшие числа фибоначи к числу {num} это числа {f_1} и {f_2}")
        elif abs(num - f_2) > abs(num - f_1):
            print(f"Ближайшее число фибоначи к числу {num} это число {f_1}")
        else:
            print(f"Ближайшее число фибоначи к числу {num} это число {f_2}")

# n = int(input("Input digit: "))

# fi = [0, 1]

# for i in range(0, n+1):
# fi.append(fi[i]+fi[i+1])
# print(fi)


# if n in fi:
# print(fi.index(n)+1)
# else:
# print(-1)