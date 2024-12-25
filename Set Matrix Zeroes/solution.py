#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        rowlength = len(mat)
        collength = len(mat[0])
        row =[0]*rowlength
        col = [0]*collength
        for i in range(rowlength):
            for j in range(collength):
                if mat[i][j]==0:
                    row[i] = 1
                    col[j] = 1
                if row[i]==1 or col[j]==1:
                    mat[i][j]=0
        return mat

...# } Driver Code Ends