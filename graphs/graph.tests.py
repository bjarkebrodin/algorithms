import unittest

from graph import Graph, IllegalGraphLoopException
# from graph import GraphGolf


class GraphTests (unittest.TestCase):
    def setUp(self):
        self.G = Graph(10)

    def test_connect_adds_connection(self):
        self.G.connect(2, 1)
        self.assertTrue(2 in self.G.adjacent(1))
        self.assertTrue(1 in self.G.adjacent(2))

    def test_connect_fails_on_loop(self):
        exception = None
        try:
            self.G.connect(2, 2)
        except IllegalGraphLoopException as e:
            excecption = e
        self.assertIsNotNone(excecption)

    def test_len(self):
        self.assertEqual(len(self.G),10)


# class GraphGolfTests (unittest.TestCase):
#     def setUp(self):
#         self.G = GraphGolf(10)

#     def test_connect_adds_connection(self):
#         self.G[2]=1
#         self.assertTrue(2 in self.G[1])
#         self.assertTrue(1 in self.G[2])

#     def test_connect_fails_on_loop(self):
#         self.G[2] = 2
#         self.assertFalse(2 in self.G[2])

#     def test_len(self):
#         self.assertEqual(len(self.G),10)




if __name__ == "__main__":
    unittest.main()
