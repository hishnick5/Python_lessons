
##4
#
input_string = input('Введите числа словами')
# Функция для перевода строчных чисел в цифровые
def transform_string_to_integer(input_string):
    # Словарь для склейки слов в числа
    number_word_dict = {
        "ты": 1000, "м": 1000000,
        "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900,
        "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19,
        "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
        "дес": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }
    # Создаём переменную с суммой
    sum = 0
    # Создаём временную переменную
    tmp = 0
    # Создаём список из слов введенных с клавиатуры
    words = input_string.split()
    # Создаём список ключей из нашего словаря
    keys = list(number_word_dict.keys())
    # Проходимся циклом по списку введённых слов
    for word in words:
        # Получаем отфильтрованный ключ с высоким значением
        # Описываю процесс в переменной: в функцию filter передаём в качестве аргумента 
        # лямбда функцию с методом строк word.startswith(x), который определяет начинается ли строка (word) со строки (x)
        # и список ключей словаря т.е. переменную keys, затем мы это всё оборачиваем в список через
        # конструкор типов list и далее берем только первый элемент в получившеся отфильтрованном списке.
        # Создаём отфильтрованный список ключей начинающихся с итерируемого префикса (части слова) с помощью лямбда функции
        # и берем только первый элемент этого списка
        filtered_key = list(filter(lambda x: word.startswith(x), keys))[0]
        
        # Достаём из нашего словаря высокое значение по отфильтрованному ключу
        number = number_word_dict[filtered_key]
        
        # Если временная переменная больше нуля и временная переменная с высоким значением больше 900
        if tmp > 0 and number > 900:
            # Умножаем number и tmp и добавляем в переменную sum
            sum += number * tmp
            # И сразу же обнуляем временную переменную
            tmp = 0
        # Иначе
        else:
            # Во временную переменную добавляем значение number(значение отфильтрованного ключа из словаря)
            tmp += number
    # В итоге возвращаем сложение переменных суммы и временной переменной
    return sum + tmp
transform_string_to_integer(input_string)