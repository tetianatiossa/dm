import itertools



def isomorphic(graph1, graph2):

    if len(graph1) != len(graph2):

        return False


    for perm in itertools.permutations(range(len(graph1))):

        is_perm = True

        for i in range(len(graph1)):

            for j in graph1[i]:

                if perm[j] not in graph2[perm[i]]:

                    is_perm = False

                    break

            if not is_perm:

                break

        if is_perm:

            return True



    return False



def modify_graph(graph):

    # Вивід початкового графа

    print("Початковий граф: ", graph)

    # Змінюємо граф тут, щоб порушити ізоморфізм

    # Наприклад, ми можемо видалити ребро між вершинами 1 і 2

    # і додати ребро між вершинами 2 і 3

    graph[1].remove(2)

    graph[2].remove(1)

    graph[2].append(3)

    graph[3].append(2)

    # Вивід модифікованого графа

    print("Модифікований граф: ", graph)

    return graph



# Приклад

graph1 = [[2, 1], [2, 2, 3], [3, 1, 3], [1, 2]]

graph2 = [[1, 2, 1], [2, 2, 3], [2, 1, 3], [1, 2]]



if isomorphic(graph1, graph2):

    print("Графи ізоморфні")

    graph2 = modify_graph(graph2)

    if isomorphic(graph1, graph2):

        print("Модифікація не спрацювала")

    else:

        print("Модифікація спрацювала")

        # Вивід модифікованого графа, якщо ізоморфізм порушено

        print("Новий граф: ", graph2)
else:

    print("Графи не ізоморфні")
