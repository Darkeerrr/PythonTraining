# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}
          ,{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
          {" VIII":" S007 "}]
print(list_1)

def value_individual_finder(list):
    empty_list =[]
    for i in list_1:
        for key, value in i.items():
            empty_list.append(value.strip())
    return set(empty_list)

print(value_individual_finder(list_1))