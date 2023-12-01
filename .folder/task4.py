# надо посчитать количество цифр введенного числа
# Timur Islamgulov 0 ->1
# Timur Islamgulov 15345 -> 5
# Timur Islamgulov 0.0001 - > 5

num = abs(float(input("Введите число: ")))
x = 0
flag = True
while flag:
    if num % 10 > 0:
        num = num * 10
        print(f"num - > {num}")
    else:
        num = num / 10
        flag = False
flag = True
while flag:
    if num == 0:
        flag = False
    else:
        x = x + 1
        num = int(num / 10)
        print(f"x -> {x} num -> {num}")
print(f"Колличество цифр в числе = {x}")