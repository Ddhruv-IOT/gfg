class Solution:
    def findUnique(self, arr):
        # code here
        num = 0
        for i in range(len(arr)):
            num ^= arr[i]
        return num

...# } Driver Code Ends