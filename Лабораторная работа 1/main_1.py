numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = 0
sum_num = sum(numbers)
len_num = len(numbers)
count_num = sum_num/len_num
numbers[4] = count_num
print("Измененный список:", numbers)
