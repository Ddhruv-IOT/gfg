#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        ans=arr[0]
        for i in range(1,len(arr)):
            ans^=(arr[i]^i)
        return ans

...# } Driver Code Ends