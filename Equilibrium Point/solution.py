# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total_sum = sum(arr)  # Calculate the total sum of the array
        left_sum = 0          # Initialize left sum to 0
        
        for i, num in enumerate(arr):
            total_sum -= num  # Update the right sum by subtracting the current element
            
            if left_sum == total_sum:  # Check if left sum equals right sum
                return i               # Return the equilibrium index
            left_sum += num  # Update the left sum
        return -1
...# } Driver Code Ends