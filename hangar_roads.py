from undirected_graph import UndirectedGraph


def calculate_cost_of_travel(costs: dict, num_visited: int, visited_sequence: list) -> float:
    """Główna funkcja, oblicza i zwraca łączny koszt przejazdu między hangarami, czyli wynik końcowy"""

    # korzystamy z funkcji pomocniczych do stworzenia grafu i listy hangarów
    hangar_graph = create_graph(costs)
    visited_sequence_by_index = translate_letters_to_indexes(visited_sequence)

    # obliczamy łączną cenę przejazdu z wykorzystaniem algorytmu dijkstry
    total_travel_cost = 0

    for i in range(num_visited - 1):
        index_of_starting_hangar = visited_sequence_by_index[i]
        index_of_ending_hangar = visited_sequence_by_index[i + 1]

        current_cost = hangar_graph.dijkstra(index_of_starting_hangar, index_of_ending_hangar)
        total_travel_cost += current_cost

    return total_travel_cost


def create_graph(costs: dict) -> UndirectedGraph:
    """
    Funkcja pomocnicza w której tworzymy graf, na podstawie rysunku w treści zadania.
    Gdyby w przyszłości rozkład dróg uległ zmianie, wystarczy zedytować tę funkcję
    """
    hangar_graph = UndirectedGraph(15)    # na rysunku jest 15 wierzchołków grafu
    red_weight = costs['r']
    green_weight = costs['g']
    blue_weight = costs['b']

    # operujemy na indeksach wierzchołków, wierzchołek A ma indeks 0, B ma indeks 1 itd.
    hangar_graph.add_edge(0, 5, blue_weight)
    hangar_graph.add_edge(0, 7, green_weight)
    hangar_graph.add_edge(1, 8, blue_weight)
    hangar_graph.add_edge(2, 4, red_weight)
    hangar_graph.add_edge(2, 12, green_weight)
    hangar_graph.add_edge(3, 11, red_weight)
    hangar_graph.add_edge(3, 14, red_weight)
    hangar_graph.add_edge(4, 5, red_weight)
    hangar_graph.add_edge(4, 6, blue_weight)
    hangar_graph.add_edge(6, 7, green_weight)
    hangar_graph.add_edge(6, 9, green_weight)
    hangar_graph.add_edge(7, 8, red_weight)
    hangar_graph.add_edge(7, 9, blue_weight)
    hangar_graph.add_edge(8, 10, blue_weight)
    hangar_graph.add_edge(8, 11, green_weight)
    hangar_graph.add_edge(9, 10, green_weight)
    hangar_graph.add_edge(9, 12, green_weight)
    hangar_graph.add_edge(9, 13, red_weight)
    hangar_graph.add_edge(10, 14, blue_weight)
    hangar_graph.add_edge(12, 13, blue_weight)
    hangar_graph.add_edge(13, 14, red_weight)

    return hangar_graph


def translate_letters_to_indexes(letter_sequence: list) -> list:
    """"Przyjmuje listę odwiedzonych hangarów opisanych literami, zwraca listę ich indeksów w macierzy sąsiedztwa"""
    alphabet_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    return [alphabet_dictionary[hangar_name] for hangar_name in letter_sequence]


def get_valid_numbers(price_prompt: str, cast_to_float: bool):
    """Przyjmuje dane wejściowe liczbowe od użytkownika - muszą one być one liczbami nieujemnymi"""
    cost = 0

    while True:
        try:
            if cast_to_float:
                cost = float(input(price_prompt))
            else:
                cost = int(input(price_prompt))
        except ValueError:
            print('Podana wartość musi być liczbą.')
            continue
        if cost < 0:
            print('Podana wartość nie może być ujemna.')
            continue
        else:
            break

    return cost


def get_valid_list(user_prompt: str, valid_hangars: list, num_of_visited_hangars: int) -> list:
    """
    Przyjmuje od użytkownika listę odwiedzonych hangarów jako string,
    sprawdza czy jest prawidłowy, oraz zamienia string na listę
    """
    while True:
        valid_string_flag = True
        visited_hangars_string = input(user_prompt).upper()
        visited_hangars_nospaces = visited_hangars_string.replace(' ', '')

        # sprawdzenie długości listy
        if len(visited_hangars_nospaces) != num_of_visited_hangars:
            print('Liczba odwiedzonych hangarów na liście musi być równa zadeklarowanej liczbie hangarów.')
            valid_string_flag = False
        else:
            # sprawdzenie poprawności symboli
            for character in visited_hangars_nospaces:
                if character not in valid_hangars:
                    print(f'Nieprawidłowa nazwa hangaru w liście - prawidłowe hangary to: {valid_hangars}')
                    valid_string_flag = False
                    break

        if valid_string_flag:
            break

    visited_hangars_sequence = [character for character in visited_hangars_nospaces]

    return visited_hangars_sequence


# Przyjmowanie parametrów liczbowych do obliczeń
red_cost = get_valid_numbers('Cena przejazdu po drodze czerwonej: ', True)
green_cost = get_valid_numbers('Cena przejazdu po drodze zielonej: ', True)
blue_cost = get_valid_numbers('Cena przejazdu po drodze niebieskiej: ', True)
number_of_visited_hangars = get_valid_numbers('Liczba odwiedzonych hangarów: ', False)

# Przyjmowanie listy hangarów do obliczeń
list_input_prompt = 'Lista odwiedzonych hangarów (oddzielone spacją): '
valid_hangars_list = ['A', 'B', 'C', 'D']
visited_hangars_list = get_valid_list(list_input_prompt, valid_hangars_list, number_of_visited_hangars)

# Uruchomienie głównej funkcji programu
costs_of_colors = {'r': red_cost, 'g': green_cost, 'b': blue_cost}  # r = red, g = green, b = blue
print(f'Cena przejazdu: {calculate_cost_of_travel(costs_of_colors, number_of_visited_hangars, visited_hangars_list)}')
