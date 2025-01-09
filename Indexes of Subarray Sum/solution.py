#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        start = 0
        current_sum = 0
    
        for end in range(len(arr)):
            # Add the current element to the window
            current_sum += arr[end]
            # Shrink the window as long as the current_sum exceeds the target
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1
            # Check if the current_sum equals the target
            if current_sum == target:
                return [start + 1, end + 1]  # 1-based indexing
        # If no subarray is found
        return [-1]

        
...# } Driver Code Ends