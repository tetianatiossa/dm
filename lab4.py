# імпортуємо бібліотеку deque з модуля collections

from collections import deque



# створюємо пустий граф

graph = []



# відкриваємо файл з вхідними даними у режимі читання

with open("data.txt", "r") as f:

    # зчитуємо кількість вершин графу

    n = int(f.readline())

    # зчитуємо матрицю суміжності графу

    for i in range(n):

        row = list(map(int, f.readline().split()))

        graph.append(row)



# задаємо джерело та стік

source = 0

sink = n - 1



# створюємо батьківський масив для зберігання шляхів

parent = [-1] * n



# ініціалізуємо максимальний потік нулем

max_flow = 0



# цикл пошуку максимального потоку

while True:

    # створюємо масив для зберігання відвіданих вершин та чергу для пошуку в ширину

    visited = [False] * n

    queue = deque([source])



    # позначаємо джерело як відвідану та його батьківський вузол як непридільний

    visited[source] = True

    parent[source] = -1



    # задаємо мінімальний пропуск для даного шляху як нескінченність

    min_flow = float("inf")



    # пошук в ширину

    while queue:

        # беремо першу вершину з черги

        u = queue.popleft()



        # проходимо по всім вершинам графу

        for v in range(n):

            # перевіряємо, чи не була відвідана ця вершина та чи існує між u та v ребро

            if not visited[v] and graph[u][v] > 0:

                # позначаємо вершину як відвідану та зберігаємо батьківський вузол

                visited[v] = True

                parent[v] = u



                # знаходимо мінімальну пропускну здатність в даному шляху

                min_flow = min(min_flow, graph[u][v])



                # якщо досягнули сток, то виходимо з циклу

            if v == sink:

                break



                # додаємо вершину до черги

            queue.append(v)



            # якщо стік не був відвіданий, то потік не може бути збільшений

            if not visited[sink]:

                break



            # додаємо мінімальний пропуск до максимального потоку

            max_flow += min_flow



            # оновлюємо пропускні здатності ребер

        v = sink

        while v != source:

            u = parent[v]

            graph[u][v] -= min_flow

            graph[v][u] += min_flow

            v = u



    print(f"Max flow: {max_flow}")
