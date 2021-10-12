from queue import PriorityQueue


class UndirectedGraph:
    """
    Klasa reprezentująca graf za pomocą macierzy sąsiedztwa (adjacency matrix), gdzie:
    wartość wynosi -1 jeśli wierzchołki są ze sobą niepowiązane oraz jest równa wadze krawędzi jeśli są połączone
    """

    def __init__(self, number_of_vertices):
        self.num_of_vertices = number_of_vertices
        self.edges = [[-1 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]
        self.visited_vertices = []

    def add_edge(self, vertex_one_index: int, vertex_two_index: int, weight) -> None:
        """
        Dodaje do grafu krawędź między dwoma podanymi wierzchołkami, o podanej wadze.
        Wpisuje wartość wagi do macierzy symetrycznie.
        """
        self.edges[vertex_one_index][vertex_two_index] = weight
        self.edges[vertex_two_index][vertex_one_index] = weight

    def dijkstra(self, start_vertex_index: int, end_vertex_index: int) -> float:
        """
        Zwraca koszt przejazdu od podanego hangaru startowego do hangaru końcowego, obliczony przy pomocy
        algorytmu Dijkstry
        """
        # resetujemy listę odwiedzonych wierzchołków po obliczaniu poprzedniego kosztu
        self.visited_vertices = []

        costs_from_start_vertex = {vertex_index: float('inf') for vertex_index in range(self.num_of_vertices)}
        costs_from_start_vertex[start_vertex_index] = 0

        queue = PriorityQueue()
        queue.put((0, start_vertex_index))

        while not queue.empty():
            (dist, current_vertex_index) = queue.get()
            self.visited_vertices.append(current_vertex_index)

            for neighbor_index in range(self.num_of_vertices):
                if self.edges[current_vertex_index][neighbor_index] != -1:
                    # oznacza to, że występuje połączenie
                    distance = self.edges[current_vertex_index][neighbor_index]

                    if neighbor_index not in self.visited_vertices:
                        # wierzchołek nie był odwiedzony więc obliczamy nowy koszt
                        old_cost = costs_from_start_vertex[neighbor_index]
                        new_cost = costs_from_start_vertex[current_vertex_index] + distance

                        if new_cost < old_cost:
                            # oznacza to, że znaleźliśmy tańsze połączenie, aktualizujemy koszt
                            queue.put((new_cost, neighbor_index))
                            costs_from_start_vertex[neighbor_index] = new_cost

        return costs_from_start_vertex[end_vertex_index]
