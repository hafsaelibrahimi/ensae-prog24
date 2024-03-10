from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, grid):
        self.grid = grid 


    def find_elem(self, elem):
        g = self.grid
        m = g.m
        n = g.n
        state = g.state

        for i in range(m):
            for j in range(n):
                if state[i][j] == elem :
                    return i, j
                
        
    def go_from_to(self, dep, arr):
        x_dep, y_dep = dep 
        x_arr, y_arr = arr
        res = []

        if x_dep > x_arr:
            for k in range(x_dep - x_arr):
                res.append(((x_dep-k, y_dep), (x_dep-k-1, y_dep)))
                (self.grid).swap((x_dep-k, y_dep), (x_dep-k-1, y_dep))
        
        elif x_dep < x_arr:
            for k in range(x_arr - x_dep):
                res.append(((x_dep+k, y_dep), (x_dep+k+1, y_dep)))
                (self.grid).swap((x_dep+k, y_dep), (x_dep+k+1, y_dep))
        
        if y_dep > y_arr:
            for k in range(y_dep - y_arr):
                res.append(((x_arr, y_dep-k), (x_arr, y_dep-k-1)))
                (self.grid).swap((x_arr, y_dep-k), (x_arr, y_dep-k-1))
        
        elif x_dep < x_arr:
            for k in range(y_arr - y_dep):
                res.append(((x_arr, y_dep+k), (x_arr, y_dep+k+1)))
                (self.grid).swap((x_arr, y_dep+k), (x_arr, y_dep+k+1))

        return res 
        

    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        n = self.grid.n
        m = self.grid.m
        state = self.grid.state
        sol = []
        x_dest, y_dest = 0, 0

        for i in range(1, n*m+1):
            x_dep, y_dep = self.find_elem(i)
            sol + self.go_from_to((x_dep, y_dep), (x_dest, y_dest))
            y_dest += 1
            if y_dest == n :
                y_dest = 0
                x_dest += 1
        return sol
