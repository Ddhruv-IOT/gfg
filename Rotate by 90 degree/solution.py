#User function Template for python3

class Solution:
    
    def rotateby90(self, mat):
        n = len(mat)
        
        # Reverse each row
        for i in range(n):
            mat[i] = mat[i][::-1]
        # Take transpose of the matrix
        for t in range(n):
            for j in range(t):
                mat[t][j], mat[j][t] = mat[j][t], mat[t][j]
...# } Driver Code Ends