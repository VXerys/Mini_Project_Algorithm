import networkx as nx

G = nx.DiGraph()

edges = [
    ('H', 'P1', 4),
    ('H', 'P2', 3),
    ('P1', 'P5', 5), 
    ('P2', 'P3', 7),
    ('P2', 'P4', 10),
    ('P3', 'P4', 2),
    ('P4', 'P5', 9),
    ('P4', 'RS', 5),
    ('P5', 'RS', 16),
]

G.add_weighted_edges_from(edges)

# Menghitung jalur terpendek dari H ke RS menggunakan Algoritma Dijkstra
shortest_path = nx.dijkstra_path(G, source='H', target='RS')
shortest_distance = nx.dijkstra_path_length(G, source='H', target='RS')

print("Jalur terpendek:", " -> ".join(shortest_path))
print("Jarak total:", shortest_distance)
