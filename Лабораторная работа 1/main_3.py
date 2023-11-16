# TODO Найдите количество книг, которое можно разместить на дискете
count_bytes_book = 100*50*25*4
count_bytes_disk = 1.44*1024*1024
count_book = round((count_bytes_disk/count_bytes_book))

print("Количество книг, помещающихся на дискету:", count_book)
