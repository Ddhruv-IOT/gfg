#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        # Sort the array
        arr.sort()
        n = len(arr)
        count = 0
        
        # Fix the largest side one by one
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                # Check if the pair satisfies the triangle inequality
                if arr[i] + arr[j] > arr[k]:
                    # If true, all pairs between i and j satisfy
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
...# } Driver Code Ends