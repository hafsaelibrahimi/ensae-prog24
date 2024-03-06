import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_Representation(unittest.TestCase):
    def test_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        grid.trace()
if __name__ == '__main__':
    unittest.main()