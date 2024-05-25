import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if colors:
        nx.set_node_attributes(tree, colors, 'color')

    node_colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(10, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def build_heap(arr):
    if not arr:
        return None

    # Створюємо вузли для кожного елемента масиву
    nodes = [Node(key) for key in arr]

    # З'єднуємо вузли, щоб побудувати бінарну купу
    for i in range(len(arr) // 2):
        if 2 * i + 1 < len(arr):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(arr):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

def generate_colors(n):
    colors = []
    for i in range(n):
        ratio = i / (n - 1) if n > 1 else 1
        red = int(ratio * 255)
        green = int(ratio * 255)
        blue = int(240 + ratio * 15)  # Зміна відтінку для більшого контрасту
        colors.append(to_hex((red / 255, green / 255, blue / 255)))
    return colors

def dfs(node, colors, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if node is None:
        return order

    visited.add(node.id)
    order.append(node.id)
    if node.left and node.left.id not in visited:
        dfs(node.left, colors, visited, order)
    if node.right and node.right.id not in visited:
        dfs(node.right, colors, visited, order)

    return order

def bfs(node, colors):
    visited = set()
    order = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        if current.id not in visited:
            visited.add(current.id)
            order.append(current.id)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return order

def visualize_traversal(tree_root, traversal_type='dfs'):
    if traversal_type == 'dfs':
        order = dfs(tree_root, [])
    elif traversal_type == 'bfs':
        order = bfs(tree_root, [])

    # Генерація кольорів
    colors = generate_colors(len(order))
    color_map = {node_id: color for node_id, color in zip(order, colors)}

    # Візуалізація дерева з кольоровим обхідним шляхом
    draw_tree(tree_root, colors=color_map)

# Приклад масиву для побудови бінарної купи
heap_array = [10, 5, 3, 2, 4, 1]

# Побудова бінарної купи
heap_root = build_heap(heap_array)

# Відображення обходу в глибину (DFS)
print("Візуалізація обходу в глибину (DFS):")
visualize_traversal(heap_root, traversal_type='dfs')

# Відображення обходу в ширину (BFS)
print("Візуалізація обходу в ширину (BFS):")
visualize_traversal(heap_root, traversal_type='bfs')
