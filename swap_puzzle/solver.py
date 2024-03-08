from grid import Grid

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def swap_solver(self, cell1, cell2):
        (x, y) = cell1
        (a, b) = cell2
        if (abs(x - a) == 1 and y == b) or (abs(y - b) == 1 and x == a):
            self.grid.swap_seq([(cell1, cell2)])
        else:
            raise ValueError("L'échange entre les cellules spécifiées n'est pas autorisé.")

    def search(self, k):
        for i in range(self.grid.m):
            for j in range(self.grid.n):
                if self.grid.state[i][j] == k:
                    return i, j
        raise ValueError("La valeur {} n'a pas été trouvée dans la grille.".format(k))

    def list_swap(self, a, b, x, y):
        swap_to_do = []
        while a != x or b != y:
            if a < x:
                swap_to_do.append(((x, y), (x - 1, y)))
                x -= 1
            elif a > x:
                swap_to_do.append(((x, y), (x + 1, y)))
                x += 1
            elif b < y:
                swap_to_do.append(((x, y), (x, y - 1)))
                y -= 1
            elif b > y:
                swap_to_do.append(((x, y), (x, y + 1)))
                y += 1
        return swap_to_do

    def get_solution(self):
        movements = []
        for k in range(1, self.grid.m * self.grid.n + 1):
            i_start, j_start = self.search(k)
            i_goal, j_goal = (k - 1) // self.grid.n, (k - 1) % self.grid.n
            for u in self.list_swap(i_goal, j_goal, i_start, j_start):
                self.swap_solver(u[0], u[1])
                movements.append(u)
        return movements

