list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_players = len(list_players)
num_players = round(num_players / 2)
first_com = list_players[:num_players]
second_com = list_players[num_players:]
print(first_com)
print(second_com)
