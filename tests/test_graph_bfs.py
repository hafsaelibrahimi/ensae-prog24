import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_GraphBFS(unittest.TestCase):
    def test_bfs(self):
        graph = Graph.graph_from_file("input/graph1.in")
        self.assertEqual(graph.bfs(1,3), 2)

if __name__ == '__main__':
    unittest.main()