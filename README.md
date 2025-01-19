# Mencari Navigasi Rumah Sakit Terpendek Menggunakan Algoritma Pencarian: Dijkstra dan A-Star

## Deskripsi Proyek
Proyek ini bertujuan untuk memecahkan masalah pencarian jalur terpendek dalam graf berbobot dengan metode algoritma Dijkstra dan A-Star. Studi kasus yang digunakan adalah menentukan rute terpendek dari rumah Aldi ke rumah sakit terdekat melalui sejumlah persimpangan jalan.

### Kelompok 5
- M. Sechan Alfarisi
- Eneng Salwa Khoerunisa
- Tresna Gunawan
- Fazri Kurniawan

**Mata Kuliah:** Kompleksitas Algoritma  
**Dosen Pengampu:** Zaaenal Alamsyah, M.Kom

---

## Algoritma yang Digunakan

### Algoritma Dijkstra
Algoritma Dijkstra adalah metode pencarian jalur terpendek berbasis greedy yang bekerja dengan mengevaluasi semua kemungkinan lintasan untuk menemukan rute optimal dalam graf berbobot non-negatif. Dalam implementasi ini:
- Graf direpresentasikan sebagai graf berarah (directed graph).
- Simpul awal adalah rumah Aldi (H) dan simpul tujuan adalah rumah sakit (RS).
- Jalur yang dihasilkan adalah **H → P2 → P3 → P4 → RS** dengan jarak total 17.

#### Kode Implementasi (Python):
```python
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
```

### Algoritma A-Star (A*)
Algoritma A-Star adalah metode pencarian jalur terpendek yang memadukan biaya perjalanan aktual (g(n)) dan estimasi heuristik ke tujuan (h(n)) untuk menemukan rute optimal. Algoritma ini sangat efisien dalam menyelesaikan masalah pencarian jalur pada graf kompleks.

- Jalur yang dihasilkan: **I → E → RS** dengan total biaya 11.

#### Kode Implementasi (Python):
```python
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
    'F': {'C': 3, 'D': 5},
    'G': {'C': 2, 'K': 3},
}

heuristics = {
    'RS': 0, 'E': 8, 'I': 6, 'L': 4, 'K': 5,
    'J': 4, 'A': 9, 'B': 7, 'C': 6, 'D': 8,
    'F': 6, 'G': 13,
}

def a_star_algorithm(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (heuristics[start], 0, start, []))

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
```

---

## Perbandingan Algoritma
| Kriteria         | Dijkstra                          | A-Star                         |
|------------------|-----------------------------------|---------------------------------|
| **Metode**       | Evaluasi semua kemungkinan jalur  | Menggabungkan g(n) dan h(n)    |
| **Kecepatan**    | Lambat pada graf besar           | Lebih cepat jika heuristik baik |
| **Heuristik**    | Tidak diperlukan                 | Sangat bergantung pada heuristik |
| **Hasil**        | Jalur pasti terpendek            | Jalur optimal lebih efisien    |

---

## Kesimpulan
Kedua algoritma memiliki keunggulan masing-masing. Algoritma Dijkstra cocok untuk graf sederhana tanpa perlu heuristik, sedangkan A-Star lebih efisien untuk graf besar dan kompleks. Dalam kasus ini:
- **Dijkstra** menghasilkan jalur: **H → P2 → P3 → P4 → RS** dengan jarak 17.
- **A-Star** menghasilkan jalur: **I → E → RS** dengan total biaya 11.

Pemilihan algoritma tergantung pada kebutuhan aplikasi dan struktur graf.

