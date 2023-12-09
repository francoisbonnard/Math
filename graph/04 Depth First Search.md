page 55
https://www.youtube.com/watch?v=7fujbpJ0LB4&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=4v

The Depth First Search (DFS) is the most fundamental search algorithm used to explore nodes and edges of a graph. It runs with a time complexity of O(V+E) and is often used as a building block in other algorithms. By itself the DFS isn’t all that useful, but when augmented to perform other tasks such as count connected components, determine connectivity, or find bridges/articulation points then DFS really shines. 

```python
# Global or class scope variables
n = number of nodes in the graph
g = adjacency list representing graph
visited = [false, …, false] # size n
function dfs(at):
    if visited[at]: return
    visited[at] = true
    neighbours = graph[at]
    for next in neighbours:
    dfs(next)
# Start DFS at node zero
start_node = 0
dfs(start_node)
```
coming from DFS-graph-traversal.md
```python
marked = [False] * G.size()
def dfs_iter(G,v):
    stack = [v]
    while len(stack) > 0:
        v= stack.pop()
        if not marked[v]:
            visit(v)
            marked[v]= True
            for w in G.neighbors(v):
                stack.append(w)
```

## connected components

