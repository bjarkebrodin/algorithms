import unittest
import sys

from time import perf_counter
from graph import Graph, IllegalGraphLoopException
from dfs import RecursiveDfs, Dfs

sys.setrecursionlimit(10**6)

class RecursiveDfsTests(unittest.TestCase):
    def setUp(self):
        self.G = Graph(10)
        self.Ga = Graph(10)
        for v in range(10):
            for q in range(10):
                if v != q: 
                    self.G[v] = q
                    if v < 9 and q < 9:
                        self.Ga[v] = q
        self.D = RecursiveDfs(self.G,0)
        self.Da = RecursiveDfs(self.Ga,0)

    def test_in_positive(self):
        self.assertTrue(1 in self.D)

    def test_in_negative(self):
        self.assertFalse(9 in self.Da)

    def test_connected_positive(self):
        self.assertTrue(self.D.is_connected())

    def test_conected_negative(self):
        self.assertFalse(self.Da.is_connected())

class DfsTests(unittest.TestCase):
    def setUp(self):
        self.G = Graph(10)
        self.Ga = Graph(10)
        for v in range(10):
            for q in range(10):
                if v != q: 
                    self.G[v] = q
                    if v < 9 and q < 9:
                        self.Ga[v] = q
        self.D = Dfs(self.G,0)
        self.Da = Dfs(self.Ga,0)

    def test_in_positive(self):
        self.assertTrue(1 in self.D)

    def test_in_negative(self):
        self.assertFalse(9 in self.Da)

    def test_connected_positive(self):
        self.assertTrue(self.D.is_connected())

    def test_conected_negative(self):
        self.assertFalse(self.Da.is_connected())


if __name__ == "__main__":
    unittest.main()
