import numpy as np

# Зчитуємо вхідний файл
with open('input.txt') as f:
    n = int(f.readline()) # кількість міст
    graph = np.zeros((n, n)) # матриця відстаней між містами
    for i in range(n):
        row = list(map(int, f.readline().split()))
        for j in range(n):
            graph[i, j] = row[j]

# Алгоритм Найближчого сусіда
visited = [0] # список відвіданих міст
current = 0 # поточне місто
path_length = 0 # довжина маршруту
while len(visited) < n:
    min_distance = float('inf')
    next_city = None
    for i in range(n):
        if i not in visited and graph[current, i] < min_distance:
            min_distance = graph[current, i]
            next_city = i
    visited.append(next_city)
    path_length += min_distance
    current = next_city
path_length += graph[visited[-1], 0] # повернення в початкове місто

# Виводимо результат
print("Маршрут:", visited)
print("Довжина маршруту:", path_length)
