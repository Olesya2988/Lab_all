# TODO  Напишите функцию count_letters
def count_letters(text):
    text_ = text.lower()
    dict_ = {}
    find_ok = False
    count_symbols = 0
    for i in text_:
        if i.isalpha():
            count_symbols += 1
            for q in dict_:
                if i == q:
                    find_ok = True
                    dict_[q] = dict_[q] + 1
            if not find_ok:
                dict_[i] = 1
        find_ok = False
    return dict_

# TODO Напишите функцию calculate_frequency


def calculate_frequency(calc_dict):
    calc_val = calc_dict.values()
    all_symbols = 0
    for num in calc_val:
        all_symbols += num
    for sym_dict in calc_dict:
        val_sym = calc_dict[sym_dict]
        val_sym = format((val_sym/all_symbols), ".2f")
        calc_dict[sym_dict] = val_sym
    return calc_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

count_dict = count_letters(main_str)
freq_dict = calculate_frequency(count_dict)
for symbols_ in freq_dict:
    val_dict = freq_dict[symbols_]
    print(f'{symbols_}: {val_dict}')
