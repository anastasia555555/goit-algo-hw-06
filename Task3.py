import networkx as nx

def create_weighted_graph():
    G = nx.Graph()

    edges = [
        ("Central", "Park", 5),
        ("Central", "Museum", 4),
        ("Central", "University", 6),
        ("Park", "Stadium", 7),
        ("Museum", "Mall", 3),
        ("University", "Mall", 4),
        ("Mall", "Airport", 10),
        ("Stadium", "Airport", 8)
    ]

    G.add_weighted_edges_from(edges)
    return G

if __name__ == "__main__":
    G = create_weighted_graph()

    print("Найкоротші шляхи від Central:")
    paths = nx.single_source_dijkstra_path(G, "Central")

    for destination, path in paths.items():
        print(f"{destination}: {path}")