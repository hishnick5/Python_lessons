# Исход
# Ставки на победителя
win = [
    {'П1':'Победа первой домашней команды'}, {'П2':'Победа второй гостевой команды'}, {'Х':'Ничья'}]

# Двойной шанс
double_chance = [
    {'1Х': 'Победа первой команды или ничья'}, {'2Х', 'Победа второй команды или ничья'},
    {'12', 'Победа первой или второй команды'}]

# Фора
# Целочисленная на 1 команду(хозяева)
integer_fora1 = [{'Ф1(0)': 'Нулевая фора на команду 1 (хозяева). При победе команды 1, ставка выигрывает, при ничье — возврат по ставке, в случае победы гостей (команда 2) — ставка проигрывает'},
                 {'Ф1(+1)': 'Фора +1 на хозяев. При победе команды 1 или ничье, ставка выигрывает, проигрыш хозяев в 1 мяч — возврат по ставке, победа гостей в 2 и более мячей — ставка проиграла.'},
                 {'Ф1(+2)': 'Фора +2 на хозяев. Ставка проигрывает при победе гостей в 3 мяча и более. Победа гостей в 2 мяча — возврат по ставке. В остальных случаях — ставка выигрывает. Аналогичные ставки — Ф1(+3), Ф1(+4)'}, 
                 {'Ф1(-1)': 'Фора -1 на команду 1. Победа хозяев в два и более мячей — выигрыш ставки. Победа хозяев в 1 мяч — возврат. В остальных случаях — проигрыш.'}, 
                 {'Ф1(-2)': 'Фора -2 на команду 1. Победа хозяев в 3 и более мячей — выигрыш ставки. Победа хозяев в 2 мяча — возврат. В остальных случаях — проигрыш.'}]
# Целочисленная на 2 команду(гости)
integer_fora2 = [{'Ф2(0)': 'Нулевая фора на команду 2 (гости). При победе команды 2, ставка выигрывает, при ничье — возврат по ставке, в случае победы хозяев (команда 1) — ставка проигрывает'}, 
                 {'Ф2(+1)': 'Фора +1 на гостей. При победе команды 2 или ничье, ставка выигрывает, проигрыш гостей в 1 мяч — возврат по ставке, победа хозяев в 2 и более мячей — ставка проиграла.'}, 
                 {'Ф2(+2)': 'Фора +2 на гостей. Ставка проигрывает при победе хозяев в 3 мяча и более. Победа хозяев в 2 мяча — возврат по ставке. В остальных случаях — ставка выигрывает. Аналогичные ставки — Ф1(+3), Ф1(+4)'}, 
                 {'Ф2(-1)': 'Фора -1 на команду 2. Победа гостей в два и более мячей — выигрыш ставки. Победа гостей в 1 мяч — возврат. В остальных случаях — проигрыш.'}, 
                 {'Ф2(-2)': 'Фора -2 на команду 2. Победа гостей в 3 и более мячей — выигрыш ставки. Победа гостей в 2 мяча — возврат. В остальных случаях — проигрыш.'}]
# Дробная фора на 1 команду(хозяева)
fractional_fora1 = [{'Ф1(+0,5)': 'Тоже самое, что 1Х (победа или ничья хозяев)'}, 
                    {'Ф1(+1,5)': 'Фора +1,5 на хозяев. При победе команды 1, ничье или проигрыше хозяев в 1 мяч, ставка выигрывает. Победа гостей в 2 и более мячей — ставка проиграла'}, 
                    {'Ф1(+2,5)': 'Фора +2,5 на хозяев. При победе гостей в 3 и более мячей, ставка проигрывает. В остальных случаях — выигрыш. Аналогичные ставки — Ф1(+3,5), Ф1(+4,5)'}, 
                    {'Ф1(-0,5)': 'Тоже самое, что П1 (победа хозяев)'}, 
                    {'Ф1(-1,5)': 'Фора -1,5 на команду 1. Победа хозяев в 2 и более мячей — выигрыш ставки. В остальных случаях — проигрыш.'},
                    {'Ф1(-2,5)': 'Фора -2,5 на команду 1. Победа хозяев в 3 и более мячей — выигрыш ставки. В остальных случаях — проигрыш.'}]
# Дробная фора на 2 команду(гости)
fractional_fora2 = [{'Ф2(+0,5)': 'Тоже самое, что 2Х (победа или ничья гостей)'}, 
                    {'Ф2(+1,5)': 'Фора +1,5 на гостей. При победе команды 2, ничье или проигрыше гостей в 1 мяч, ставка выигрывает. Победа хозяев в 2 и более мячей — ставка проиграла'}, 
                    {'Ф2(+2,5)': 'Фора +2,5 на гостей. При победе хозяев в 3 и более мячей, ставка проигрывает. В остальных случаях — выигрыш. Аналогичные ставки — Ф2(+3,5), Ф2(+4,5)'}, 
                    {'Ф2(-0,5)': 'Тоже самое, что П2 (победа гостей)'}, 
                    {'Ф2(-1,5)': 'Фора -1,5 на команду 2. Победа гостей в 2 и более мячей — выигрыш ставки. В остальных случаях — проигрыш.'},
                    {'Ф2(-2,5)': 'Фора -2,5 на команду 2. Победа гостей в 3 и более мячей — выигрыш ставки. В остальных случаях — проигрыш.'}]
# Азиатская фора на 1 команду(хозяева)
asian_fora1 = [{'Ф1(+0,25), Ф1(0,+0.5)': 'Фора +0,25 на хозяев (К1). Победа К1 принесет выигрыш всей ставки. Ничья — возврат по 1/2 ставки и выигрыш по 1/2 ставки. Победа гостей приведёт к проигрышу всей ставки. Аналогичные ставки — Ф1(+1,25), Ф1(+2,25)'}, 
               {'Ф1(+0,25), Ф1(0,+0.5)': 'Фора +0,75 на хозяев. Победа К1 или ничья принесет выигрыш всей ставки. Победа гостей в 1 мяч — возврат по 1/2 ставки и проигрыш по 1/2 ставки. Победа гостей в 2 и более мячей приведёт к проигрышу всей ставки. Аналогичные ставки — Ф1(+1,75), Ф1(+2,75)'}, 
               {'Ф1(-0,25), Ф1(0,-0.5)': 'Фора -0,25 на хозяев. При победе К1, ставка выигрывает. Ничья — возврат 1/2 ставки. Победа гостей — проигрыш ставки. Аналогичные ставки — Ф1(-1,25), Ф1(-2,25)'}, 
               {'Ф1(-0,75), Ф1(-0.5,-1)': 'Фора -0,75 на хозяев. Победа К1 в 2 и более мячей — выигрыш ставки. Победа хозяев в 1 мяч — выигрыш по 1/2 ставки. В остальных случаях — проигрыш. Аналогичные ставки — Ф1(-1,75), Ф1(-2,75)'}]
# Азиатская фора на 2 команду(гости)
asian_fora2 = [{'Ф2(+0,25), Ф2(0,+0.5)': 'Фора +0,25 на гостей (К2). Победа К2 принесет выигрыш всей ставки. Ничья — возврат по 1/2 ставки и выигрыш по 1/2 ставки. Победа хозяев приведёт к проигрышу всей ставки. Аналогичные ставки — Ф2(+1,25), Ф2(+2,25)'}, 
               {'Ф2(+0,25), Ф2(0,+0.5)': 'Фора +0,75 на гостей. Победа К2 или ничья принесет выигрыш всей ставки. Победа хозяев в 1 мяч — возврат по 1/2 ставки и проигрыш по 1/2 ставки. Победа хозяев в 2 и более мячей приведёт к проигрышу всей ставки. Аналогичные ставки — Ф2(+1,75), Ф2(+2,75)'}, 
               {'Ф2(-0,25), Ф2(0,-0.5)': 'Фора -0,25 на гостей. При победе К2, ставка выигрывает. Ничья — возврат 1/2 ставки. Победа хозяев — проигрыш ставки. Аналогичные ставки — Ф2(-1,25), Ф2(-2,25)'}, 
               {'Ф2(-0,75), Ф2(-0.5,-1)': 'Фора -0,75 на гостей. Победа К2 в 2 и более мячей — выигрыш ставки. Победа гостей в 1 мяч — выигрыш по 1/2 ставки. В остальных случаях — проигрыш. Аналогичные ставки — Ф2(-1,75), Ф2(-2,75)'}]

# Тотал Больше
# Целочисленный тотал
integer_total = [{'ТБ(1)': 'Если в матче 2 и более мячей — выигрыш. Забьют 1 гол — возврат по ставке. Нет голов — проигрыш.'}, 
                 {'ТБ(2)': 'Если в матче 3 и более мячей — выигрыш. Забьют 2 гола — возврат по ставке. Ноль голов или 1 — проигрыш.'}, 
                 {'ТБ(3)': 'Если в матче 4 и более мячей — выигрыш. Забьют 3 гола — возврат по ставке. 1 или 2 голов — проигрыш.'}, 
                 {'ТБ(4)': 'Если в матче 5 и более мячей — выигрыш. Забьют 4 гола — возврат по ставке. 2 или 3 голов — проигрыш.'}, 
                 {'ТБ(5)': 'Если в матче 6 и более мячей — выигрыш. Забьют 5 гола — возврат по ставке. 3 или 4 голов — проигрыш.'}]
# Дробный тотал
fractional_total = [{'ТБ(0,5)': 'Выигрыш в случае 1 и более мячей в матче'}, 
                    {'ТБ(1,5)': 'Выигрыш, если забито 2 и более мячей'}, 
                    {'ТБ(2,5)': 'Ставка выигрывает, если забьют 3 и более мячей.'}, 
                    {'ТБ(3,5)': 'Ставка выигрывает, если забьют 4 и более мячей.'}, 
                    {'ТБ(4,5)': 'Ставка выигрывает, если забьют 5 и более мячей.'}]
# Азиатский тотал
asian_total = [{'': ''}, {'': ''}, {'': ''}, {'': ''}, {'': ''}]
# Индивидуальный тотал на 1 команду(хозяева)
individual_total1 = [{'': ''}, {'': ''}, {'': ''}, {'': ''}, {'': ''}]
# индивидуальный тотал на 2 команду(гости)
individual_total2 = [{'': ''}, {'': ''}, {'': ''}, {'': ''}, {'': ''}]

# Голы
goal = [{'': ''}, {'': ''}, {'': ''}, {'': ''}, {'': ''}]

# 