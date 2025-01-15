# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
    
        cumulative_sum = 0
        max_length = 0
        prefix_sums = {}
        for i, num in enumerate(arr):
            # Update cumulative sum
            cumulative_sum += num
            # Check if cumulative sum itself is equal to k
            if cumulative_sum == k:
                max_length = i + 1
            # Check if (cumulative_sum - k) exists in the prefix_sums dictionary
            if (cumulative_sum - k) in prefix_sums:
                max_length = max(max_length, i - prefix_sums[cumulative_sum - k])
            # Store the cumulative sum in the dictionary if not already present
            if cumulative_sum not in prefix_sums:
                prefix_sums[cumulative_sum] = i
        return max_length
...# } Driver Code Ends