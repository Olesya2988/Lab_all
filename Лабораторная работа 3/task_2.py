# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, delimiter=","):
    list_1 = set(str_1.split(delimiter))
    list_2 = str_2.split(delimiter)
    inter_list = list(list_1.intersection(list_2))
    inter_list.sort()
    return inter_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
