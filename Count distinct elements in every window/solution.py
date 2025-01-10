
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        if k > n:
            return []
    
        result = []
        # Loop through each window
        for i in range(n - k + 1):
            # Create a set for the current window
            window_set = set(arr[i:i + k])
            # Add the size of the set (distinct count) to the result
            result.append(len(window_set))
        return result
...# } Driver Code Ends