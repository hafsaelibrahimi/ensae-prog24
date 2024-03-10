import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_Heuristique(unittest.TestCase):
    def test_heuristique0(self):
         g = Grid.grid_from_file("input/grid0.in")
         self.assertEqual(g.heuristique(),2)
    def test_heuristique1(self):
         g = Grid.grid_from_file("input/grid1.in")
         self.assertEqual(g.heuristique(),1)
    def test_heuristique3(self):
         g = Grid.grid_from_file("input/grid3.in")
         self.assertEqual(g.heuristique(),4)
    def test_heuristique4(self):
         g = Grid.grid_from_file("input/grid4.in")
         self.assertEqual(g.heuristique(),12)

if __name__ == '__main__':
    unittest.main()