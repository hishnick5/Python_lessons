

# Импортируем библиотеку для выполнения HTTP-запросов в интернет
import requests
from math import log

# Читаем текстовый файл по url-ссылке
data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text

# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']
# 
# 
# Превращаем список в множество, удаляя дублирующиеся слова
word_set = set(data)
# Удаляем из множества слово, символизирующее раздел между главами
word_set.discard('[new chapter]')
# Выводим результаты
# print('Общее количество слов: {}'.format(len(data)))
# print('Общее количество уникальных слов: {}'.format(len(word_set)))

# Инициализируем пустой словарь
word_counts = {}
# Инициализируем количество глав
count_chapter = 0
# Создаем цикл по всем словам из списка слов
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, то увеличиваем количество глав на 1
        count_chapter += 1
        # Переходим на новую итерацию цикла
        continue
    # Проверяем, что текущего слова еще нет в словаре слов
    if word not in word_counts:
        # Если условие выполняется, инициализируем новый ключ 1
        word_counts[word] = 1
    else:
        # В противном случае, увеличиваем количество слов на 1
        word_counts[word] += 1

# Выводим количество глав
# print('Количество глав: {}'.format(count_chapter))

# Создаем цикл по ключам и их порядковым номерам полученного словаря
'''for i, key in enumerate(word_counts):
    # Выводим только первые 10 слов
    if i == 10:
        break
    print(key, word_counts[key])'''

# Инициализируем общий список, в котором будем хранить списки слов в каждой главе
chapter_data = []
# Инициализируем список слов, в котором будет хранить слова одной главы
chapter_words = []

# Создаем цикл по всем словам из списка
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, добавляем список со словами из главы в общий список
        chapter_data.append(chapter_words)
        # Обновляем (перезаписываем) список со словами из текущей главы
        chapter_words = []
    else:
        # В противном случае, добавляем текущее слово в список со словами из главы
        chapter_words.append(word)

# Проверяем, что у нас получилось столько же списков, сколько глав в произведении
# print('Вложенный список содержит {} внутренних списка'.format(len(chapter_data)))с
# Выведем первые 100 слов 0-ой главы
# print(chapter_data[0][:100])

# Инициализируем список, в котором будем хранить словари
chapter_words_count = []

# Создаем цикл по элементам внешнего списка со словами
for chapter_words in chapter_data:
    # Инициализируем пустой словарь, куда будем добавлять результаты
    temp = {}
    # Создаем цикл по элементам внутреннего списка
    for word in chapter_words:
        # Проверяем, что текущего слова еще нет в словаре
        if word not in temp:
            # Если условие выполняется, добавляем ключ в словарь
            temp[word] = 1
        else:
            # В противном случае, увеличиваем количество влождений слова в главу
            temp[word] += 1
    # Добавляем получившийся словарь в список
    chapter_words_count.append(temp)
# Выводим результат
# print(chapter_words_count)

# Задание 1
'''
Давайте введем понятие частоты употребления отдельного слова в документе (term frequency, или tf).
В нашем случае речь идёт не о документах, а о главах книги
(выше мы писали, что в текстовом документе главы разделяются строкой '[new chapter]').
Формула для вычисления term frequency для слова word:
tf_word,chapter=n_word,chapter/n_chapter
где:
n_word,chapter  - сколько раз слово word встрачается в главе chapter
n_chapter  - количество слов в главе chapter
Например, слово "гостья" употребляется в 15-ой главе 10 раз (nword,chapter).
(кстати, главы у нас нумеруются с 0). Общее количество слов в тексте 15-ой главы - 1359 (nchapter). 
Тогда:
tf_гостья,15=10/1359≈0.007358
'''
# Задание:
'''
Напишите программу, которая позволит получать частоту употребления любого заданного слова target_word
в заданной главе target_chapter.

Дополнительное требование:

Пострайтесь сделать программу максимально обобщенной. То есть желательно 
рассчитать характеристику tf для всех слов из каждой главы, чтобы 
впоследствии не было необходимости производить вычисления снова.

Подсказка:

Для этого вы можете для каждой главы создать словарь, 
ключами которого являются слова, а значения - частота употребления этого слова в этой главе
'''
# Инициализируем пока пустой список словарей для данных tf
tf_dict_list = []
# Создаём цикл по индексам и элементам из списка со 171 словарями(главами) chapter_words_count
for i, chapter in enumerate(chapter_words_count):
    # Создаём словарь ключами которого будут являться слова из главы,
    # а значениями tf-частота употребления этого слова в текущей главе
    tf_dict = {}
    # Создаём цикл по словам из итовой главы
    for tf_word in chapter:
        # Вносим в словарь, слово и частоту употребления tf по формуле 
        tf_dict[tf_word] = chapter[tf_word] / len(chapter_data[i])
    # Заносим в список наш словарь с tf-частотой слов
    tf_dict_list.append(tf_dict)
# Проверим наш код
# target_word = 'гостья'
# target_chapter = 15
# print(tf_dict_list[target_chapter][target_word])

# Задание 2
# Пришло время познакомиться с понятием document frequency.
'''
Document frequency (для удобства сократим до df) — это доля документов,
в которых встречается искомое слово.
Формула df:   df_word=N_word/N
где:
N_word  - число документов (глав) содержащих слово word
N  - общее число документов (глав)
Объясним на примере: 
наш текст состоит из 171 главы ( N ), а слово "человек" встречается в 115 главах.
Тогда: df_человек=115/171≈0.6725
'''
# Задание:
'''
Напишите программу, которая позволит вычислять document frequency для заданного слова target_word
и выведить результат на экран.
Дополнительное требование:
Пострайтесь сделать программу максимально обобщенной. То есть желательно
рассчитать характеристику df для всех уникальных слов из книги, чтобы впоследствии 
не было необходимости производить вычисления снова.
Подсказка: Для этого вы можете создать словарь, ключами которого являются слова из книги, 
а значения - доля документов, содержащих эти слова
'''

# Инициализируем новый словарь df
df_dict = {}
# Создаём цикл по элементам из списка со 171 словарями(главами) chapter_words_count
for chapter in chapter_words_count:
    # Создаём цикл по словам из итевого словаря
    for word in set(chapter):
        # Если слова нету в новом словаре
        if word not in df_dict:
            # Заносим с словарь это слово со значением в виде формулы вычисления df
            df_dict[word] = 1 / count_chapter
        # В противном случае(если итовое слово там уже есть)
        else:
            # Добавляем к значению этого слова формулу вычисления df
            df_dict[word] += 1 / count_chapter
# Тестовая программа для проверки поиска определённого слова в определённой главе
# target_word = 'человек'
# print(df_dict[target_word])


# Задание 3
# Пришло время дать разъяснения: для чего мы делали вычисления выше и что нас ждет впереди?
'''
Если какое-то слово часто употребляется в документе, то, вероятно, этот документ что-то 
рассказывает о предмете/действии, описываемом этим словом. Скажем, если вы читаете книгу, 
в которой много раз употребляется слово "заяц", то, вероятно, эта книга про зайцев.

Однако, если вы возьмёте слово "и", то оно будет встречаться почти в каждой книге много раз.

Таким образом, если мы хотим найти наиболее значимые слова в книге, мы, с одной стороны,
хотим найти наиболее частые слова, а с другой — убрать те, которые не несут важной информации, 
так как встречаются везде.

Такая задача хорошо решается с помощью 
tf-idf — статистической метрики для оценки важности слова в тексте. Другими словами, 
tf-idf — это «контрастность» слова в документе (насколько оно выделяется среди других слов).

Формула для вычисления следующая:

tf-idf = term frequency * inverse document frequency

tf — это частотность термина, которая измеряет, насколько часто термин встречается в документе.

idf — это обратная документная частотность термина. 
Она измеряет непосредственно важность термина во всём множестве документов.

Чтобы получить idf, необходимо поделить 1 на полученную в Задании 2 документную частоту (df):

idf=1/df 

Мы будем использовать не сырые значения idf, а их логарифмы, то есть  tf∗log(idf) . 
Сейчас мы не будем заострять внимания на том, почему следует использовать именно логарифм 
— это долгий разговор. Вернемся к нему, когда будем изучать методы 
машинного обучения для обработки текстов. Подробнее о tf-idf вы можете почитать здесь.

В качестве примера измерим tf-idf слова "анна" в главе 4. Слово "анна" встречается 
в указанной главе 7 раз, при этом в 4 главе 1060 слов, всего же 
слово "анна" упоминается в 32 главах из 171.

Таким образом, tf-idf данного слова в данной главе будет равно:

tf_idfанна,4=tf∗log(1df)=71060∗log(17132)≈0.011067 

Примечание: здесь используется натуральный логарифм по основанию  e , 
однако в общем случае основание логарифма не имеет значения, 
так как характеристика tf-idf используется для сравнения контрастности слов между собой
'''

# Создаём список словарей со значениями tf-idf для каждого слова в главе
tf_idf_dict_list = []
# Создаём цикл по индексам и элементам(главам) предыдущего списка со словарями данных tf_dict_list
for i, chap in enumerate(tf_dict_list):
    # Создаём временный словарь tf-idf для каждого слова в этой главе
    tf_idf_dict = {}
    # Создаём цикл по словам в итовой главе
    for word in chap:
        # Заносим во временный словарь слово и присваеваем ему значение по формуле: tf*log(1/df)
        tf_idf_dict[word] = tf_dict_list[i][word]*log(1/df_dict[word])
    # Заносим в наш список получившийся словарь по текущей главе
    tf_idf_dict_list.append(tf_idf_dict)

# Программа для поиска определённого слова в определённой главе
# target_word = 'анна'
# target_chapter = 4
# print(tf_idf_dict_list[target_chapter][target_word])

# Задание 4
'''
Теперь, когда мы умеем вычислять tf-idf для каждого слова в главе, мы можем найти те слова, 
которые являются самыми «контрастными» для данной главы, то есть они 
могут являться в своём роде заголовком для главы.

Например, для главы 3 наиболее значимыми словами будут:

"анна", "павловна", "функе"
'''
# Задание:
'''
Напишите программу, которая позволяет вывести три слова, имеющие 
самое высокое значение tf-idf в заданной главе target_chapter в порядке убывания tf-idf.
'''

target_chapter = 3
# Используем функцию сортировки sorted
# Нашёл способ как отсортировать словарь по значению
# Создаём рейтинг-список с отсортироваными словами по убыванию
sorted_ftidf = sorted(
    tf_idf_dict_list[target_chapter],
    key=tf_idf_dict_list[target_chapter].get,
    reverse=True)

# Выводим первые 3 контрастных слова 
print(sorted_ftidf[:3])

# P.S.
'''
Я тут попытался сделать из списка word_set словарь содержащий ключи ввиде слов  
и значения в скольких главах повторяется это слово, но тут возможно я сделал что то не то, 
очень долго обрабатывает данные, а может быть и верно написал )))
# Создаем словарь
df_dict = {}
# создаем цикл по уникальным словам
for word in word_set:
    # Создаем цикл по списоку из 171 списка chapter_data
    for chapter in chapter_data:
        # Если итовое слово есть в итовой главе
        if word in set(chapter):
            # Проверяем, если в словаре нету этого слова
            if word not in df_dict:
                # Заносим с словарь это слово со значением в виде формулы вычисления df
                df_dict[word]= 1/count_chapter
            else: # В противном случае(если итовое слово там уже есть)
                # Добавляем к значению этого слова формулу вычисления df
                df_dict[word]+= 1/count_chapter
# Проверим наш код
target_word = 'человек'
print(df_dict[target_word])
'''
