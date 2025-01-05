...# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        n = len(arr)
        
        # Step 2: Initialize two pointers and the count
        i, j = 0, n - 1
        count = 0
        # Step 3: Use two-pointer approach
        while i < j:
            if arr[i] + arr[j] < target:
                # All pairs between i and j are valid
                count += (j - i)
                i += 1  # Move the left pointer forward
            else:
                j -= 1  # Move the right pointer backward
        return count