import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_GridBFS(unittest.TestCase):
    def test_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        initial_tuple = Grid.tuple_from_grid(g)
        final_tuple = tuple([i for i in range(1,g.n * g.m+1)])  
        shortest_path_length = g.find_path_grille(initial_tuple, final_tuple)
        print(shortest_path_length)
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        initial_tuple = Grid.tuple_from_grid(g)
        final_tuple = tuple([i for i in range(1,g.n * g.m+1)])  
        shortest_path_length = g.find_path_grille(initial_tuple, final_tuple)
        print(shortest_path_length)
if __name__ == '__main__':
    unittest.main()