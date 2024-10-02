n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
dx, dy, x, y = 0, 1, 0, 0

for i in range(1, n * m + 1):
    matrix[x][y] = i
    if matrix[(x + dx) % n][(y + dy) % m]:
        dx, dy = dy, -dx
    x += dx
    y += dy    
for line in matrix:
    print(*(f'{i:<3}' for i in line), sep='')
print(matrix)

# ну что продолжаем наше обучение

"""
приоритет арифметических операций:
1) операции в скобках ( )
2) возведение в степень '**'
3) Создание отрицательного числа, смена знака '+,-'
4) Умножение и деление '* /'
5) Целочисленное деление 'div' '//'
6) Остаток от деления или 
деление по модулю 'mod' '%'
7) Сложение и вычитание '+,-'
"""

# PYTHON-4. Циклы. Задание 4.8
# Напишите код, который определяет, является ли
# вложенный список test_matrix квадратной матрицей
# (то есть матрицей, у которой количество строк
# равно количеству столбцов).
test_matrix = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1],
    [123, 5, 1]
]
is_square = None
if len(test_matrix) == len(test_matrix[0]):
    is_square=True
else:
    is_square=False
print(is_square)
