# задача 1 сложная необязательная 
# Посчитать сумму цифр любого целого или вещественного числа, 
# число вводит пользователь.
# Через строку решать нельзя.
num = abs(float(input("Введите число: ")))
x = 0
y = 0
while num % 10 > 0 :
    num = num * 10
while num > 0:
    y = int(num % 10)
    x = x + y
    num = int(num / 10)
    print(f"y -> {y} x -> {x} num -> {num}")
print(x)