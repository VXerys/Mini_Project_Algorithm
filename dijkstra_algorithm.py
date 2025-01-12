import heapq
from typing import Dict, List, Tuple

class Graph:
    def __init__(self):
        # Inisialisasi graf kosong
        self.graph = {}

    def add_edge(self, u: str, v: str, weight: int):
        """
        Menambahkan sisi berbobot ke dalam graf.
        
        :param u: Simpul asal
        :param v: Simpul tujuan
        :param weight: Bobot sisi
        """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Jika graf tidak berarah

    def dijkstra(self, start: str) -> Dict[str, int]:
        """
        Implementasi algoritma Dijkstra untuk mencari jarak terpendek dari simpul awal.

        :param start: Simpul awal
        :return: Dictionary berisi jarak terpendek dari simpul awal ke simpul lain
        """
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (jarak, simpul)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 1)
graph.add_edge('C', 'B', 2)
graph.add_edge('B', 'D', 1)
graph.add_edge('C', 'D', 5)

start_node = 'A'
shortest_distances = graph.dijkstra(start_node)

print(f"Jarak terpendek dari simpul {start_node}:")
for node, distance in shortest_distances.items():
    print(f"{start_node} -> {node}: {distance}")
