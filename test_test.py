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
# создаем список тестовый
rerenew_list = [45,78,12,96,85,74,23,12]

# создаем три переменные
a = 10
b = 58
c = 214

# суммируем переменные
d = a + b + c
