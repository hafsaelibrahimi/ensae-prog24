import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_Astar(unittest.TestCase):
    def test_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        print(g.Astar())
    def test_grid1(self): 
        g=Grid.grid_from_file("input/grid1.in")
        print(g.Astar())
if __name__ == '__main__':
    unittest.main()