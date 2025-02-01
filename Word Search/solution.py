class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        
        visited = [[False]*m for i in range(n)]
        def rec(mat, i, j, word, k):
            if k == len(word):
                return True
                
            if 0 <= i < n and 0 <= j < m and not visited[i][j]:
                if mat[i][j] == word[k]:
                    visited[i][j] = True
                    ans = (
                        rec(mat, i-1, j, word, k+1) or
                        rec(mat, i+1, j, word, k+1) or
                        rec(mat, i, j-1, word, k+1) or
                        rec(mat, i, j+1, word, k+1)
                        )
                    visited[i][j] = False
                    return ans
               
            return False
        for i in range(n):
            for j in range(m):
                if rec(mat, i, j, word, 0):
                    return True
        return False

...# } Driver Code Ends