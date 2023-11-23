# TODO Напишите функцию для поиска индекса товара
def find_product(list_product, product):
    find_ok = False
    index_product = 0
    for i in range(len(list_product)):
        if list_product[i] == product and not find_ok:
            find_ok = True
            index_product = i
        else:
            continue
    if find_ok:
        return index_product
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_product(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

