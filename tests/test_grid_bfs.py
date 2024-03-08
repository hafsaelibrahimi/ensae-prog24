import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph
class Test_GridBFS(unittest.TestCase):
    def test_grid1(self):
            g = Grid.grid_from_file("input/grid0.in")
        gra = g.grid_to_graph()
        print(gra)
if __name__ == '__main__':
    unittest.main()