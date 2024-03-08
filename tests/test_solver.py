import sys 
sys.path.append("swap_puzzle/")

import unittest 

from grid import Grid
from solver import Solver 

class Test_Solver(unittest.TestCase):
    def test_solver1(self):
        g = Grid.grid_from_file("input/grid1.in")
        s = Solver(g)
        s.get_solution()
        self.assertEqual(g.is_sorted(), True)

    def test_solver2(self):
        g = Grid.grid_from_file("input/grid2.in")
        s = Solver(g)
        s.get_solution()
        self.assertEqual(g.is_sorted(), True)

    def test_solver3(self):
        g = Grid.grid_from_file("input/grid3.in")
        s = Solver(g)
        s.get_solution()
        self.assertEqual(g.is_sorted(), True)
    
    def test_solver4(self):
        g = Grid.grid_from_file("input/grid4.in")
        s = Solver(g)
        s.get_solution()
        self.assertEqual(g.is_sorted(), True)

if __name__ == '__main__':
    unittest.main()
