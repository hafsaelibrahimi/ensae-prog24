"""
This is the grid module. It contains the Grid class and its associated methods.
"""
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np
import random

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
            permutations_of_remainder = generate_permutations(remaining_elements)
            for perm in permutations_of_remainder:
                results.append((first_element,) + perm)
        return results
    
    def voisin(self, tupl):
        liste_tuple = []
        for i in range(self.m): 
            for j in range(self.n):
                liste_tuple.append(list(tupl[j*self.n : j*self.n+self.n])) # Correction de cette ligne
        voisin = []
        for i in range(self.m):  
            for j in range(self.n):
                if j + 1 < self.n:
                    # Swap horizontal
                    new_grid = Grid(self.m, self.n, liste_tuple)
                    new_grid.swap((i, j), (i, j+1))
                    voisin.append(new_grid)
                if i + 1 < self.m:
                    # Swap vertical
                    new_grid = Grid(self.m, self.n, liste_tuple)
                    new_grid.swap((i, j), (i+1, j))
                    voisin.append(new_grid)
        return voisin
    def grid_to_graph(self):
        numbers_list = [i for i in range(1, self.n*self.m+1)]
        numbers_tuple = tuple(numbers_list)
        graph = Graph(self.permutation (numbers_tuple))
        for nod in graph.nodes:
            voisins = self.from_ch_to_grid(nod).tvoisins()
            for v in voisins:
                if (nod, v) not in graph.edges and (v, nod) not in graph.edges:
                    graph.add_edge(v, nod)
        return graph

    def find_path_grille(graph, initial_tuple, target_tuple):
        # Trouver toutes les permutations du tuple initial
        permutations = self.generate_permutations(tuple_initial)

        # Créer un dictionnaire pour stocker les voisins de chaque permutation
        neighbors_dict = {}

        for perm in permutations:
            # Trouver les voisins de chaque permutation
            neighbors = self.voisin(perm)
            neighbors_dict[perm] = neighbors

        # Trouver le plus court chemin entre le tuple initial et le tuple cible
        shortest_path = graph.bfs(tuple_initial, target_tuple)

        return neighbors_dict, shortest_path







