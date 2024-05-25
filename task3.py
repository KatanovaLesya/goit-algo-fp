import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))  # Якщо граф не орієнтований

def dijkstra(graph, start):
    # Ініціалізація
    heap = []
    heapq.heappush(heap, (0, start))
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    shortest_path_tree = {}

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Якщо знайдена більша відстань, пропустити
        if current_distance > distances[current_vertex]:
            continue

        # Перевірити всі суміжні вершини
        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдена коротша відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                shortest_path_tree[neighbor] = current_vertex

    return distances, shortest_path_tree

def visualize_graph(graph, start_vertex, distances, shortest_path_tree):
    G = nx.Graph()

    # Додавання ребер до графа NetworkX
    for vertex in graph.vertices:
        for neighbor, weight in graph.vertices[vertex]:
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Розташування вершин на площині

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Відзначаємо найкоротші шляхи
    for vertex in shortest_path_tree:
        nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path_tree[vertex], vertex)], edge_color='r', width=2)

    plt.title(f"Найкоротші шляхи від вершини {start_vertex}")
    plt.show()

# Приклад використання
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_vertex = 'A'
    distances, shortest_path_tree = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex in distances:
        print(f"Відстань до {vertex}: {distances[vertex]}")
    
    print("\nДерева найкоротших шляхів:")
    for vertex in shortest_path_tree:
        print(f"Вершина {vertex} досягнута через {shortest_path_tree[vertex]}")

    # Візуалізація графа та найкоротших шляхів
    visualize_graph(graph, start_vertex, distances, shortest_path_tree)
