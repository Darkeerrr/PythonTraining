# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
n = abs(int(input("Введите число: ")))
i = 1
Fac = 1
if n == 0:
    print(f"{n}")
else:
    while i != n + 1:
        Fac *= i
        i += 1
        print(f"Fac -> {Fac} , i -> {i}")
print(f"Факториал числа {n} равен {Fac}")

# while n > 0:
#     Fac = Fac * n
#     n -=1
#     print(f"Fac -> {Fac} , n -> {n}")
# print(Fac)