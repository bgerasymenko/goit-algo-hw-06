#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
import argparse

def build_transport_network():
    # Простий приклад: мережа станцій метро
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


def visualize_graph(G, output_image='network.png'):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=800,
            node_color="#89CFF0", edge_color="#333333", font_weight="bold")
    plt.title("Міська транспортна мережа")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_image)
    print(f"Graph image saved to {output_image}")


def generate_readme(n, m, degrees, avg_deg, isolated,
                     image_path='network.png', readme_path='README.md'):
    lines = []
    lines.append('# Завдання 1: Модель реальної мережі')
    lines.append('')
    lines.append('## Опис')
    lines.append('Модель спрощеної міської транспортної мережі — станції метро як вершини, ' +
                 'з’єднання між ними як ребра.')
    lines.append('')
    lines.append('## Візуалізація')
    lines.append(f'![Мережа]({image_path})')
    lines.append('')
    lines.append('## Основні характеристики')
    lines.append(f'- Кількість вершин: **{n}**')
    lines.append(f'- Кількість ребер: **{m}**')
    lines.append('- Ступінь вершин:')
    for node, deg in degrees.items():
        lines.append(f'  - {node}: {deg}')
    lines.append(f'- Середній ступінь вершини: **{avg_deg:.2f}**')
    iso = ', '.join(isolated) if isolated else 'відсутні'
    lines.append(f'- Ізольовані вершини: **{iso}**')
    lines.append('')
    lines.append('## Висновок')
    lines.append('Модель зв’язна, всі станції мають принаймні одне з’єднання. ' +
                 'Структура мережі доволі рівномірна.')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README generated: {readme_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Task 1: build, analyze, visualize transport network and generate README'
    )
    parser.add_argument('--image', default='network.png',
                        help='Output path for network visualization image')
    parser.add_argument('--readme', default='README.md',
                        help='Output path for README file')
    args = parser.parse_args()

    G = build_transport_network()
    n, m, degrees, avg_deg, isolated = analyze_graph(G)
    visualize_graph(G, args.image)
    generate_readme(n, m, degrees, avg_deg, isolated,
                    args.image, args.readme)

if __name__ == '__main__':
    main()
