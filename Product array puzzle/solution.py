#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        if n == 0:
            return []
    
        # Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n
        # Build prefix product array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * arr[i - 1]
        # Build suffix product array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i + 1]
        # Construct the result array
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
...# } Driver Code Ends