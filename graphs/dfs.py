import typing

from graph import Graph


"""
I value simple code here, for algorithmic clarity shorthand terminology:
- M: marker

additionally for brevity we say that:
- some vertex v is "in" a run of DFS iff. v was visited during the search
- the "length" of a DFS is the amount of vertices visited during the search
"""


class RecursiveDfs:
    # O(len(G)) + O(V+E) [init + search]
    def __init__(self, G: Graph, v: int) -> None:
        self.G = G
        self.M = [False] * len(G)
        self.Mc = 0
        self.search(v)

    def search(self, v: int) -> None:  # O(V+E)
        self.M[v] = True
        self.Mc += 1
        for q in self.G[v]:
            if not self.M[q]:
                self.search(q)

    def __contains__(self, v: int) -> bool:  # O(1)
        return self.M[v]

    def __len__(self) -> int:  # O(1)
        return self.Mc

    def has_path(self, q: int) -> bool:  # O(1)
        return self[q]

    def is_connected(self) -> bool:  # O(1)
        return len(self.M) == len(self)


"""
note that for undirected graphs we can infer that 
G.has_path(a) and G.has_path(b) => G.has_path_between(a,b)
additionally we trivially have that
G.is_connected() => G.has_path_between(a,b) for all (a,b)
"""


class Dfs:
    # O(len(G)) + O(V+E) [init + search]
    def __init__(self, G: Graph, v: int) -> None:
        self.G = G
        self.M = [False] * len(G)
        self.Mc = 0
        self.search(v)

    def search(self, v: int) -> None:  # O(V+E)
        stack = []
        stack.append(v)
        while len(stack) > 0:
            v = stack.pop()
            for q in self.G[v]:
                if not self.M[q]:
                    self.Mc += 1
                    self.M[q] = True
                    stack.append(q)

    def __contains__(self, v: int) -> bool:  # O(1)
        return self.M[v]

    def __len__(self) -> int:  # O(1)
        return self.Mc

    def has_path(self, q: int) -> bool:  # O(1)
        return self[q]

    def is_connected(self) -> bool:  # O(1)
        return len(self.G) == len(self)