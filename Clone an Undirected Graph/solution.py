#User function Template for python3

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
from collections import deque
class Solution():
    def cloneGraph(self, node):
        q=deque()
        q.append(node)
        visited=set()
        visited.add(node)
        new_node=Node(node.val)
        d=dict()
        d[node]=new_node
        while q:
            u=q.popleft()
            new_u=d.get(u)
            for v in u.neighbors:
                new_v=d.get(v,Node(v.val))
                d[v]=new_v
                new_u.neighbors.append(new_v)
                if v not in visited:
                    q.append(v)
                    visited.add(v)
        return new_node
...# } Driver Code Ends