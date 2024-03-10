"""
This is the grid module. It contains the Grid class and its associated methods.
"""
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np
import random
import heapq
from collections import deque
class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        if self.state == [list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)] :
            return True
        return False

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        (x,y) = cell1
        (a,b) = cell2
        if (abs(x-a) == 1 and y==b) or (abs(y-b) == 1 and x==a):
            self.state[x][y] , self.state[a][b] = self.state[a][b] , self.state[x][y]
        else:
            raise ValueError("L'échange entre les cellules spécifiées n'est pas autorisé.")
        return self.state

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for s in cell_pair_list :
            (cell1 , cell2) = s
            self.swap(cell1,cell2)
        return self.state

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
#Question 4 : Représentation graphique 
    def trace (self):
        fig, ax=plt.subplots()
        valeur_min, valeur_max = 1, self.n*self.m
        for i in range(self.m):
            for j in range(self.n):
                c = self.state[i][j]
                ax.text(i+0.5, j+0.5, str(c), va='center', ha='center')
        plt.matshow(self.state, cmap=plt.cm.Blues)
        ax.set_xlim(valeur_min, valeur_max)
        ax.set_ylim(valeur_min, valeur_max)
        ax.set_xticks(np.arange(valeur_max))
        ax.set_yticks(np.arange(valeur_max))
        ax.grid()
        plt.show()
#Question 6: Nous proposons de représenter chaque grille sous forme de tuple.
    def tuple_from_grid(self):
        tuple = ()
        for i in range (self.m):
            for j in range (self.n):
                tuple = tuple + (self.state[i][j],)
        return tuple
#Question 8: 
#D'abord nous allons déterminer tous les états possibles de la grille
    def generate_permutations(tup):
        if len(tup) <= 1:
            return [tup]  # Si le tuple contient un seul élément, retourner ce tuple
        results = []
        for i in range(len(tup)):
            first_element = tup[i]
            remaining_elements = tup[:i] + tup[i+1:]
            permutations_of_remainder = Grid.generate_permutations(remaining_elements)
            for perm in permutations_of_remainder:
                results.append((first_element,) + perm)
        return results
    
        
    def voisin(self, tupl):
        voisins = []
        for i in range(self.m):
            for j in range(self.n):
            # Swap horizontal
                if j + 1 < self.n:
                    new_tuple = list(tupl)
                    new_tuple[i * self.n + j], new_tuple[i * self.n + j + 1] = new_tuple[i * self.n + j + 1], new_tuple[i * self.n + j]
                    voisins.append(tuple(new_tuple))
            # Swap vertical
                if i + 1 < self.m:
                    new_tuple = list(tupl)
                    new_tuple[i * self.n + j], new_tuple[(i + 1) * self.n + j] = new_tuple[(i + 1) * self.n + j], new_tuple[i * self.n + j]
                    voisins.append(tuple(new_tuple))
        return voisins


    def find_path_grille(self, initial_tuple, target_tuple):
    # Générer toutes les permutations du tuple initial
        permutations = Grid.generate_permutations(initial_tuple)

    # Créer une nouvelle instance de graph
        graph = Graph()

    # Ajouter des nœuds au graphe pour chaque permutation
        for perm in permutations:
            graph.graph[perm] = []

    # Ajouter des arêtes au graphe en fonction des voisins
        for perm in permutations:
            voisins = self.voisin(perm)
            for voisin in voisins:
                graph.add_edge(perm, voisin)

    # Utiliser BFS sur le graphe pour trouver le chemin le plus court
        longueur_chemin_plus_court = graph.bfs_deque(initial_tuple, target_tuple)

        return longueur_chemin_plus_court
    def heuristique(self):
        weight = 0
        for i in range(self.m):
            for j in range(self.n):
                # Calcul de la position attendue pour le nombre actuel
                expected_row = (self.state[i][j] - 1) // self.n
                expected_col = (self.state[i][j] - 1) % self.n
                weight += abs(i - expected_row) + abs(j - expected_col)
        return weight // 2
    def heuristique2(self, state):
        weight = 0
        for i in range(self.m):
            for j in range(self.n):
            # Calcul de la position attendue pour le nombre actuel
                expected_row = (state[i * self.n + j] - 1) // self.n
                expected_col = (state[i * self.n + j] - 1) % self.n
                weight += abs(i - expected_row) + abs(j - expected_col)
        return weight // 2
    def Astar(self):
        dst = tuple(range(1, self.n * self.m + 1))
        tupl_grille = self.tuple_from_grid()
        permutations = Grid.generate_permutations(tupl_grille)
        graph = Graph()
        # Ajouter des nœuds au graphe pour chaque permutation
        for perm in permutations:
            graph.graph[perm] = []
        # Ajouter des arêtes au graphe en fonction des voisins
        for perm in permutations:
            voisins = self.voisin(perm)
            for voisin in voisins:
                graph.add_edge(perm, voisin)
        paths = {tupl_grille: []}
        priority_queue = [(self.heuristique(), perm) for perm in permutations]
        while priority_queue:
            cost, current_state = heapq.heappop(priority_queue)
            if current_state == dst:
                return [tupl_grille]+paths[current_state] 
            # Parcourir les voisins de l'état actuel dans le graphe
            for neighbor in graph.graph[current_state]:
                # Calculer le coût heuristique pour le voisin
                neighbor_cost = self.heuristique2(neighbor)

                # Vérifier si le voisin n'a pas encore été visité ou si un chemin plus court a été trouvé
                if neighbor not in paths or len(paths[neighbor]) > len(paths[current_state]) + 1:
                    # Mettre à jour le chemin jusqu'au voisin
                    paths[neighbor] = paths[current_state] + [neighbor]

                    # Ajouter le voisin à la file de priorité avec son coût estimé
                    heapq.heappush(priority_queue, (neighbor_cost, neighbor))

        # Si aucun chemin optimal n'a été trouvé, retourner None
        return None

    def play(grid):
        moves = 0
        while not grid.is_sorted():
            print("Current Grid:")
            for row in grid.state:
                print(row)
            print("Enter the coordinates of the cells you want to swap (x1 y1 x2 y2):")
            x1, y1, x2, y2 = map(int, input().split())
            grid.swap((x1, y1), (x2, y2))
            moves += 1
        print("Congratulations! You solved the puzzle in", moves, "moves. You could have solved it in", len(Graph(Grid.generate_permutation(sorted)).Astar(g,sorted)), "moves."

 
    def generate_grids(m, n):
        grids_by_difficulty = [[] for _ in range(4)]

        max_heuristic = (m * n) * (m + n) // 2
        heuristic_step = max_heuristic // 4

        for i in range(m * n):
            for j in range(m * n):
                initial_state = [[i * n + j + 1 for j in range(n)] for i in range(m)]
                flat_state = [num for sublist in initial_state for num in sublist]
                random.shuffle(flat_state)
                initial_state = [flat_state[i * n:(i + 1) * n] for i in range(m)]
                grid = Grid(m, n, initial_state)
                heuristic_value = grid.heuristic()

            # Trouver le niveau de difficulté
                difficulty_level = min(4, heuristic_value // heuristic_step)
                grids_by_difficulty[difficulty_level].append(grid)

        return grids_by_difficulty

# Fonction pour choisir une grille en fonction du niveau de difficulté
    def choose_grid(difficulty):
        return random.choice(generate_grids(m,n)[difficulty])

# Pour jouer à un certain niveau de difficulé

    def play_difficulty(difficulty):
        play(choose_grid(difficulty)


    def generate_swap_sequences(grids):
        swap_sequences = []

        for i in range(len(grids) - 1):
            current_grid = grids[i]
            next_grid = grids[i + 1]

            swap_sequence = find_swap_sequence(current_grid, next_grid)
            swap_sequences.append(swap_sequence)

        return swap_sequences

    def find_swap_sequence(tuple1, tuple2):
        swap = ((),())
        grid1 = list(tuple1)
        grid2 = list(tuple2)
        for i, num1 in enumerate(grid1):
            if num1 != grid2[i]:
                for j, num2 in enumerate(grid1):
                    if num2 == grid2[i]:
                        swap = ((i, (i % self.n)), j, (j % self.n))
                        break
        return swap
