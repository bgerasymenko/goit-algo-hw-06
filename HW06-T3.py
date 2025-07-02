#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
import argparse
from collections import deque
import heapq

# -------- Task 1: Build, analyze, visualize transport network --------
def build_transport_network(weighted=False):
    G = nx.Graph()
    stations = [
        "Central", "Parkside", "Museum", "Riverside",
        "University", "Airport", "Harbor"
    ]
    G.add_nodes_from(stations)
    # edges with weights (e.g., distances)
    edges = [
        ("Central", "Parkside", 5),
        ("Central", "Museum", 7),
        ("Parkside", "Riverside", 3),
        ("Museum", "University", 6),
        ("University", "Airport", 10),
        ("Riverside", "Harbor", 8),
        ("Harbor", "Airport", 4)
    ]
    if weighted:
        for u, v, w in edges:
            G.add_edge(u, v, weight=w)
    else:
        for u, v, w in edges:
            G.add_edge(u, v)
    return G


def analyze_graph(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    degrees = dict(G.degree())
    avg_deg = sum(degrees.values()) / n
    isolated = [node for node, deg in degrees.items() if deg == 0]
    return n, m, degrees, avg_deg, isolated


def visualize_graph(G, output_image):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=800,
            node_color="#89CFF0", edge_color="#333333", font_weight="bold")
    plt.title("Міська транспортна мережа")
    plt.axis('off')
    plt.tight_layout(pad=0.5)
    plt.savefig(output_image)
    print(f"Graph image saved to {output_image}")


def generate_readme_task1(n, m, degrees, avg_deg, isolated,
                           image_path, readme_path):
    lines = [
        '# Завдання 1: Модель реальної мережі',
        '',
        '## Опис',
        'Модель спрощеної міської транспортної мережі — станції метро як вершини, з’єднання як ребра.',
        '',
        '## Візуалізація',
        f'![Мережа]({image_path})',
        '',
        '## Основні характеристики',
        f'- Кількість вершин: **{n}**',
        f'- Кількість ребер: **{m}**',
        '- Ступінь вершин:'
    ]
    for node, deg in degrees.items():
        lines.append(f'  - {node}: {deg}')
    lines.append(f'- Середній ступінь вершини: **{avg_deg:.2f}**')
    iso = ', '.join(isolated) if isolated else 'відсутні'
    lines.append(f'- Ізольовані вершини: **{iso}**')
    lines.append('')
    lines.append('## Висновок')
    lines.append('Мережа зв’язна, кожна станція має принаймні одне з’єднання; структура рівномірна.')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README for Task1 generated: {readme_path}")

# -------- Task 2: DFS vs BFS path finding --------
def dfs_path(G, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return [start]
    for neighbor in G.neighbors(start):
        if neighbor not in visited:
            path = dfs_path(G, neighbor, goal, visited)
            if path is not None and path[-1] == goal:
                return [start] + path
    return None


def bfs_path(G, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


def generate_readme_task2(dfs_path_result, bfs_path_result, readme_path):
    lines = [
        '# Завдання 2: Порівняння DFS та BFS',
        '',
        '## Шлях між Central і Airport',
        '',
        f'- DFS path: `{" -> ".join(dfs_path_result)}`',
        f'- BFS path: `{" -> ".join(bfs_path_result)}`',
        '',
        '## Пояснення',
        '- **DFS** йде в глибину, обходячи кожну гілку повністю перед поверненням.',
        '- **BFS** знаходить найкоротший шлях за кількістю ребер.',
        '',
        '## Висновок',
        'DFS може знайти будь-який шлях, але не гарантує найкоротший; BFS гарантує мінімальні переходи.'
    ]
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README for Task2 generated: {readme_path}")

# -------- Task 3: Dijkstra's algorithm --------
def dijkstra(G, source):
    dist = {node: float('inf') for node in G.nodes()}
    prev = {node: None for node in G.nodes()}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, data in G[u].items():
            w = data.get('weight', 1)
            alt = d + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))
    return dist, prev


def generate_readme_task3(distances, readme_path):
    lines = [
        '# Завдання 3: Алгоритм Дейкстри',
        '',
        '## Найкоротші відстані між усіма вершинами',
        ''
    ]
    for src, dist in distances.items():
        lines.append(f'### Від джерела {src}')
        for tgt, d in dist.items():
            lines.append(f'- до {tgt}: {d}')
        lines.append('')
    lines.append('## Висновок')
    lines.append('Реалізовано алгоритм Дейкстри для зваженого графа; отримано довжини найкоротших шляхів.')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README for Task3 generated: {readme_path}")


def main():
    parser = argparse.ArgumentParser(description='Automation for Tasks 1-3')
    parser.add_argument('--image1', default='network.png', help='Task1 graph image')
    parser.add_argument('--readme1', default='README_Task1.md', help='Task1 README')
    parser.add_argument('--readme2', default='README_Task2.md', help='Task2 README')
    parser.add_argument('--readme3', default='README_Task3.md', help='Task3 README')
    args = parser.parse_args()

    # Task 1
    G = build_transport_network()
    n, m, degrees, avg_deg, isolated = analyze_graph(G)
    visualize_graph(G, args.image1)
    generate_readme_task1(n, m, degrees, avg_deg, isolated, args.image1, args.readme1)

    # Task 2
    start, goal = 'Central', 'Airport'
    dfs_res = dfs_path(G, start, goal)
    bfs_res = bfs_path(G, start, goal)
    print(f"DFS path: {dfs_res}")
    print(f"BFS path: {bfs_res}")
    generate_readme_task2(dfs_res, bfs_res, args.readme2)

    # Task 3
    Gw = build_transport_network(weighted=True)
    distances = {}
    for node in Gw.nodes():
        dist, _ = dijkstra(Gw, node)
        distances[node] = dist
    generate_readme_task3(distances, args.readme3)

if __name__ == '__main__':
    main()
