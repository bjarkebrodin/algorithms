
I am well aware these are all completely intelligeble for other people, tha

##### Graphs

###### Undirected simple graph with loops allowed
```python3
class Graph:
  def __init__(G,n):G.A=[set() for i in range(n)]
  def __getitem__(G,v):return G.A[v]
  def __len__(G):return len(G.A)
  def __setitem__(G,v,q):G[v].add(q);G[q].add(v)
```