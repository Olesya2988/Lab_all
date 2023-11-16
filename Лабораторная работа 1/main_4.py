users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

all_go = len(users)
uni_go = len(set(users))
dic_users = {
        "Общее количество": 0,
        "Уникальные посещения": 0
            }
dic_users["Общее количество"] = all_go
dic_users["Уникальные посещения"] = uni_go
print(dic_users)
