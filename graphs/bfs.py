import typing

from graph import Graph
from queue import Queue

class Bfs:
    def __init__(self, G: Graph, v: int) -> None: # O(V) + O(V+E) [init+search]
        self.G = G
        self.M = [False] * len(G)
        self.Mc = 0
        self.search(v)

    def search(self, v: int) -> None:  # O(V+E)
        queue = Queue()
        queue.put(v)
        while not queue.empty() > 0:
            v = queue.get()
            for q in self.G[v]:
                if not self.M[q]:
                    self.Mc += 1
                    self.M[q] = True
                    queue.put(q)

    def __contains__(self, v: int) -> bool:  # O(1)
        return self.M[v]

    def __len__(self) -> int:  # O(1)
        return self.Mc

    def has_path(self, q: int) -> bool:  # O(1)
        return self[q]

    def is_connected(self) -> bool:  # O(1)
        return len(self.G) == len(self)

