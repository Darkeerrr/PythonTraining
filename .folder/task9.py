# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
a = abs(int(input("Сколько арбузов на прилавке? : ")))
list_1 = list()
import random
def random_a(small, big):
    i = 0
    while i < a:
        num = random.randint(small, big)
        list_1.append(num)
        i+=1
    return list_1
print(random_a(1,10))
max_a = list_1[0]
min_a = list_1[0]
for i in range(len(list_1)):
    if max_a < list_1[i]:
        max_a = list_1[i]
    elif max_a == list_1[i]:
        max_a = list_1[i]
    else:
        min_a = list_1[i]
print(f"Арбуз для тёщи весит -> {min_a}, Мой арбуз весит -> {max_a}")