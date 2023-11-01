# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group1,group2,divider=","):
    lisr_group_1 = set(group1.split(divider))
    lisr_group_2 = set(group2.split(divider))
    common_participants = lisr_group_1.intersection(lisr_group_2)
    common_participants = list(common_participants)
    common_participants.sort()
    return common_participants

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,"|"))
