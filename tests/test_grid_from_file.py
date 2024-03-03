# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_GridLoading(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.m, 4)
        self.assertEqual(g.n, 2)
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])
    def test_swap_seq(self):
        g = Grid.grid_from_file("input/grid1.in")
        g.swap_seq([((0, 0), (1, 0)), ((2, 0), (2, 1))])
        expected_state = [[3, 2], [1, 4], [6, 5], [8, 7]]
        self.assertEqual(g.state, expected_state)


if __name__ == '__main__':
    unittest.main()
