import heapq

graph = {
    'RS': {'E': 3, 'A': 7, 'B': 2},
    'A': {'RS': 7, 'B': 3, 'D': 4},
    'B': {'RS': 2, 'A': 3, 'C': 1},
    'C': {'B': 1, 'G': 2, 'F': 3},
    'D': {'A': 4, 'B': 4, 'F': 5},
    'E': {'RS': 3, 'I': 2},
    'I': {'E': 2, 'J': 4, 'L': 4},
    'L': {'I': 4, 'J': 6, 'K': 4},
    'K': {'L': 4, 'G': 3},
    'J': {'I': 4, 'L': 6},
    'F': {'C': 3, 'G': 2},
    'G': {'F': 2},
}

heuristics = {
    'RS': 0, 'E': 8, 'I': 6, 'L': 4, 'K': 5,
    'J': 4, 'A': 9, 'B': 7, 'C': 6, 'D': 8,
    'F': 6, 'G': 13,
}

def a_star_algorithm(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (heuristics[start], 0, start, []))  # (f, g, current, path)

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            total_cost = g + heuristics[start]  
            return path + [current], total_cost
       
        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue

            g_neighbor = g + cost
            f_neighbor = g_neighbor + heuristics[neighbor]

            heapq.heappush(open_list, (f_neighbor, g_neighbor, neighbor, path + [current]))

    return None, float('inf')

start_node = 'I'  
goal_node = 'RS'  

shortest_path, total_cost = a_star_algorithm(graph, heuristics, start_node, goal_node)

print("Jalur terpendek:", " -> ".join(shortest_path))
print("Biaya total:", total_cost)
