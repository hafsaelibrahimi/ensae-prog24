from grid import Grid

class Solver:
    def __init__(self, m, n, grid):
        self.m = m
        self.n = n
        self.grid = grid
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        movements = []

        while not self.grid.is_sorted():
            for i in range(self.m):
                for j in range(self.n - 1):  # Ne pas traiter le dernier élément de la ligne
                    if self.grid.state[i][j] > self.grid.state[i][j + 1]:
                        self.grid.swap((i, j), (i, j + 1))
                        movements.append(((i, j), (i, j + 1)))

            for i in range(self.m - 1):  # Ne pas traiter la dernière ligne
                for j in range(self.n):
                    if self.grid.state[i][j] > self.grid.state[i + 1][j]:
                        self.grid.swap((i, j), (i + 1, j))
                        movements.append(((i, j), (i + 1, j)))

        return movements
