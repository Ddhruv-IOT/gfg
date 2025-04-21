#User function Template for python3
class Solution:
    def missingNum(self, arr):
        n=len(arr)
        ans=n+1
        for i in range(n):
            ans^=(arr[i]^(i+1))
        return ans

...# } Driver Code Ends