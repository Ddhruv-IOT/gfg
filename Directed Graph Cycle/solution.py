
class Solution:
    def isCycle(self, V, edges):
        # Create adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
        
        visited = [False] * V
        recursion_stack = [False] * V
        def has_cycle(node):
            visited[node] = True
            recursion_stack[node] = True
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if has_cycle(neighbor):
                        return True
                elif recursion_stack[neighbor]:
                    return True
            recursion_stack[node] = False
            return False
        for i in range(V):
            if not visited[i]:
                if has_cycle(i):
        return False
...# } Driver Code Ends