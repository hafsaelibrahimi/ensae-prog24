from grid import Grid
#Question 3:
class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, m, n, grid):
        self.m = m
        self.n = n
        self.grid = grid


    def swap_solver(self, cell1, cell2):
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
            print(a,b)
            self.grid[x][y] , self.grid[a][b] = self.grid[a][b] , self.grid[x][y]
        else:
            raise ValueError("L'échange entre les cellules spécifiées n'est pas autorisé.")
    
    def search(self,k):
        for i in range(self.m):
            for j in range(self.n):
                if self.grid [i][j] == k:
                    return i , j

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
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        movements = []
        for k in range(1,self.n*self.m +1):
            i_start = 0
            j_start = 0
            for i in range(self.m):
                for j in range(self.n):
                    if self.grid[i][j] == k:
                        i_start = i 
                        j_start = j
            j_goal = (k % self.n) -1
            i_goal = (k -j-1)// self.n 
            for u in self.list_swap(i_goal, j_goal, i_start, j_start) : 
                self.swap_solver(u[0], u[1])
                movements.append(u)
        return movements


