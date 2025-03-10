class Solution:
    def editDistance(self, str1, str2):
        # Code here
        m = len(str1)
        n = len(str2)
        
        # Create a 2D DP array with dimensions (m+1) x (n+1)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
       
        # Initialize the DP array
        for i in range(m+1):
            for j in range(n+1):
                # If the first string is empty, we need to insert all characters of the second string
                if i == 0:
                    dp[i][j] = j
                # If the second string is empty, we need to remove all characters of the first string
                elif j == 0:
                    dp[i][j] = i
                # If the characters are the same, no new operation is needed
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # If the characters are different, consider all possibilities and take the minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],     # Insert
                                       dp[i-1][j],     # Remove
                                       dp[i-1][j-1])   # Replace
        return dp[m][n]

...# } Driver Code Ends