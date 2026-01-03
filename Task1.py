import networkx as nx
import matplotlib.pyplot as plt

def create_transport_graph():
    G = nx.Graph()

    stations = [
        "Central", "Park", "Museum", "University",
        "Airport", "Stadium", "Mall"
    ]

    edges = [
        ("Central", "Park"),
        ("Central", "Museum"),
        ("Central", "University"),
        ("Park", "Stadium"),
        ("Museum", "Mall"),
        ("University", "Mall"),
        ("Mall", "Airport"),
        ("Stadium", "Airport")
    ]

    G.add_nodes_from(stations)
    G.add_edges_from(edges)

    return G

def analyze_graph(G):
    print("Кількість вершин:", G.number_of_nodes())
    print("Кількість ребер:", G.number_of_edges())
    print("\nСтупінь вершин:")
    for node, degree in G.degree():
        print(f"{node}: {degree}")

def visualize_graph(G):
    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G, pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        font_size=10
    )
    plt.title("Транспортна мережа міста")
    plt.show()

if __name__ == "__main__":
    graph = create_transport_graph()
    analyze_graph(graph)
    visualize_graph(graph)
