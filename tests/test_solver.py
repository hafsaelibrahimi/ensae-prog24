import sys 
sys.path.append("swap_puzzle/")
import unittest
from grid import Grid
from solver import Solver

class TestSolver(unittest.TestCase):
    def test_get_solution_grid1(self):
        # Charger la grille à partir du fichier grid1.in
        grid1 = Grid.grid_from_file("input/grid1.in")
        
        # Créer une instance de Solver pour résoudre la grille
        solver = Solver(grid1.m, grid1.n, grid1)
        
        # Obtenir la solution
        solution = solver.get_solution()
        grid1.swap_seq(solution)
        # Vérifier si la grille est triée après l'application de la solution
        self.assertTrue(grid1.is_sorted())

if __name__ == '__main__':
    unittest.main()
