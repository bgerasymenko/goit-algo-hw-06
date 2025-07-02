#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
import argparse
from collections import deque

# -------- Task 1: Build, analyze, visualize transport network --------
def build_transport_network():
    G = nx.Graph()
    stations = [
        "Central", "Parkside", "Museum", "Riverside",
        "University", "Airport", "Harbor"
    ]
    G.add_nodes_from(stations)
    edges = [
        ("Central", "Parkside"),
        ("Central", "Museum"),
        ("Parkside", "Riverside"),
        ("Museum", "University"),
        ("University", "Airport"),
        ("Riverside", "Harbor"),
        ("Harbor", "Airport")
    ]
    G.add_edges_from(edges)
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
            if path is not None:
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


def main():
    parser = argparse.ArgumentParser(description='Tasks 1 & 2 automation')
    parser.add_argument('--image1', default='network.png', help='Task1 graph image path')
    parser.add_argument('--readme1', default='README_Task1.md', help='Task1 README path')
    parser.add_argument('--readme2', default='README_Task2.md', help='Task2 README path')
    args = parser.parse_args()

    # Task 1 execution
    G = build_transport_network()
    n, m, degrees, avg_deg, isolated = analyze_graph(G)
    visualize_graph(G, args.image1)
    generate_readme_task1(n, m, degrees, avg_deg, isolated, args.image1, args.readme1)

    # Task 2 execution
    start, goal = 'Central', 'Airport'
    dfs_result = dfs_path(G, start, goal)
    bfs_result = bfs_path(G, start, goal)
    print(f"DFS path: {dfs_result}")
    print(f"BFS path: {bfs_result}")
    generate_readme_task2(dfs_result, bfs_result, args.readme2)

if __name__ == '__main__':
    main()
