# list_1 = [1,2,3,5,8,15,23,38]
# new_list = list()
# def find_nums(list_1):
#     for i in list_1:
#         if i % 2 == 0:
#             new_list.append((i, i**2))
#     return new_list

# print(find_nums(list_1))




# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# new_list = select(int, list_1)
# new_list = where(lambda x: x % 2 == 0, new_list)
# print(new_list)
# new_list = list(select(lambda x: (x, x**2), new_list))
# print(new_list)

n = [x for x in range(1, 20)]
print(n)