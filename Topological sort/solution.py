class Solution:
    
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges: adj[u].append(v)
        vis, res = [0]*V, []
        def dfs(n):
            vis[n] = 1
            for nei in adj[n]:
                if not vis[nei]: dfs(nei)
            res.append(n)
        for i in range(V):
            if not vis[i]: dfs(i)
        return res[::-1]

...# } Driver Code Ends