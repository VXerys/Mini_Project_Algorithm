import heapq

graph = {
    'RS': {'E': 3},
    'E': {'RS': 3, 'I': 2},
    'I': {'E': 2, 'J': 4, 'L': 6},
    'L': {'I': 6, 'K': 4},
    'K': {'L': 4},
    'J': {'I': 4},
    'A': {'RS': 7, 'B': 3, 'D': 4},
    'B': {'A': 3, 'C': 1},
    'C': {'B': 1, 'D': 6, 'F': 3},
    'D': {'A': 4, 'C': 6},
    'F': {'C': 3, 'G': 2},
    'G': {'F': 2},
}

heuristics = {
    'RS': 0, 'E': 3, 'I': 6, 'L': 10, 'K': 13,
    'J': 7, 'A': 22, 'B': 18, 'C': 13, 'D': 20,
    'F': 11, 'G': 13,
}

def a_star_algorithm(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, []))  # (f, g, current, path)

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path + [current], g
        closed_list.add(current)
        
        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue

            g_neighbor = g + cost
            f_neighbor = g_neighbor + heuristics[neighbor]

            heapq.heappush(open_list, (f_neighbor, g_neighbor, neighbor, path + [current]))

    return None, float('inf')

shortest_path, total_cost = a_star_algorithm(graph, heuristics, 'RS', 'I')

print("Jalur terpendek:", " -> ".join(shortest_path))
print("Biaya total:", total_cost)
