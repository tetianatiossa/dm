import networkx as nx



# Відкриваємо файл

with open('input.txt', 'r') as f:

    # Зчитуємо к-сть нодів

    num_nodes = int(f.readline().strip())



    # Створюємо матрицю

    matrix = []

    for i in range(num_nodes):

        matrix.append(list(map(int, f.readline().strip().split())))



# Створюємо граф

G = nx.DiGraph()



# Додаємо ребра до графіка



for i in range(num_nodes):

    for j in range(num_nodes):

        if matrix[i][j] != 0:

            G.add_edge(i, j, weight=matrix[i][j])



# Перетворюємо орієнтований граф на неорієнтований

G_undirected = G.to_undirected()



# Знаходимо Ейлерів контур

eulerian_circuit = list(nx.algorithms.euler.eulerian_circuit(G))



# Знаходимо всі цикли

cycles = list(nx.algorithms.cycles.cycle_basis(G_undirected))



# Об’єднуємо цикли в один шлях

path = []

for edge in eulerian_circuit:

    u, v = edge

    path.append(u)

    if [u, v] in cycles:

        path.append(v)



# Додаємо останню нову до шляху

path.append(path[0])



# Рахуємо загальну відстань

total_dist = sum(matrix[u][v] for u, v in zip(path[:-1], path[1:]))



# Вивід

print("Мінімальна відстань:", total_dist)

print("Шлях:", path)
