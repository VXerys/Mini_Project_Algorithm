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
**Deskripsi**: 
Algoritma Dijkstra adalah algoritma pencarian jalur terpendek yang bekerja dengan mengevaluasi semua lintasan dalam graf berbobot non-negatif. Algoritma ini menggunakan pendekatan greedy, di mana setiap langkah memilih simpul dengan jarak terpendek dari simpul awal untuk dilanjutkan. Algoritma ini menjamin hasil yang optimal pada graf berbobot non-negatif.

#### Implementasi
1. **Library NetworkX**:
   - **Kenapa menggunakan NetworkX?** Library ini menyediakan fungsi bawaan untuk manipulasi graf, sehingga mempermudah representasi graf berarah dan bobotnya.
   - Fungsi `dijkstra_path` digunakan untuk menemukan jalur terpendek, dan `dijkstra_path_length` untuk menghitung jarak total jalur tersebut.

2. **Representasi Graf**:
   - Node pada graf melambangkan titik-titik seperti rumah (H), persimpangan jalan (P1, P2, dst.), dan rumah sakit (RS).
   - Edge (sisi) pada graf memiliki bobot yang merepresentasikan jarak antar node.

3. **Kode Python**:
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

4. **Hasil**:
   - Jalur Terpendek: `H -> P2 -> P3 -> P4 -> RS`
   - Jarak Total: `17`

#### Kelebihan dan Kekurangan Dijkstra
- **Kelebihan**: Hasil yang optimal dan pasti untuk graf berbobot non-negatif.
- **Kekurangan**: Kurang efisien pada graf yang besar karena memeriksa semua kemungkinan lintasan.

---

### Algoritma A-Star (A*)
**Deskripsi**: 
Algoritma A-Star adalah metode pencarian jalur terpendek yang menggabungkan pendekatan greedy dan heuristik untuk meningkatkan efisiensi. Fungsi evaluasi utama yang digunakan adalah:
\[ f(n) = g(n) + h(n) \]
- **g(n)**: Biaya dari simpul awal ke simpul saat ini.
- **h(n)**: Perkiraan biaya dari simpul saat ini ke simpul tujuan (heuristik).

Algoritma ini efektif pada graf besar karena membatasi evaluasi hanya pada simpul yang diprediksi relevan oleh heuristik.

#### Implementasi
1. **Graf dan Heuristik**:
   - Graf melambangkan jaringan jalan dengan bobot sebagai biaya perjalanan antar simpul.
   - Fungsi heuristik `h(n)` merepresentasikan estimasi jarak ke tujuan. Dalam studi kasus ini, nilai heuristik ditentukan berdasarkan jarak geometris atau estimasi sederhana.

2. **Langkah Utama**:
   - **Inisialisasi**: Memulai dari simpul awal (I) dengan nilai heuristik awal.
   - **Evaluasi Tetangga**: Untuk setiap simpul tetangga, menghitung nilai `f(n)` berdasarkan biaya perjalanan aktual dan estimasi ke tujuan.
   - **Pencarian Jalur**: Proses berlanjut hingga simpul tujuan tercapai.

3. **Kode Python**:
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
            total_cost = g  # Biaya total dihitung dari simpul awal ke tujuan
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

4. **Hasil**:
   - Jalur Terpendek: `I -> E -> RS`
   - Total Biaya: `11`

#### Kelebihan dan Kekurangan A-Star
- **Kelebihan**: Efisien untuk graf besar karena memanfaatkan heuristik.
- **Kekurangan**: Keakuratan bergantung pada kualitas fungsi heuristik yang digunakan.

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

