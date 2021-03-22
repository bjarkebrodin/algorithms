import typing


class IllegalGraphLoopException(Exception):
    pass


"""
Implements the mathematical abstraction of a simple graph
I value simple code here, for algorithmic clarity shorthand terminology:
- n: size of graph
- v: a vertex
- q: alternative vertex
- A: adjacent

Additionally, the construct len(Graph) is interpreted as the span of the graph,
that is: the amount of vertices of the graph

let
V: the set of all vertices
E: the set of all edges

then graph gives us the following rough complexities

Init                        O(V)
Connect                     O(1)* <- under uniform hashing assumption
Check if v,q are adjacent   O(1)
Find minimal neighbour      O(E)

*amortized
"""

class Graph():

    def __init__(self, n: int) -> None:
        self.A = [set() for i in range(n)]

    def __setitem__(self, v: int, q: int) -> None:
        self.connect(v, q)

    def __getitem__(self, v: int) -> set[int]:
        return self.A[v]

    def __len__(self) -> int:
        return len(self.A)

    def connect(self, v: int, q: int) -> None:
        if v == q:
            raise IllegalGraphLoopException(type(self).__name__)

        self.A[v].add(q)
        self.A[q].add(v)

    def adjacent(self, v) -> set[int]:
        return self[v]


# class GraphGolf:
#     def __init__(G,n):
#         G.A=[set() for i in range(n)]
#     def __getitem__(G,v):
#         return G.A[v]
#     def __len__(G):
#         return len(G.A)
#     def __setitem__(G,v,q):
#         if v!=q:
#             G[v].add(q)
#             G[q].add(v)

"""
Do Variants: 
- dynamically allocated vertexlist
- ordered adjacency lists


Idea: 
fibonacci heaps and sets in tandem for theoretically superior complexity of adjancency queries???
"""
