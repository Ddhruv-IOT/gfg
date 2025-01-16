class Solution:
    def maxLen(self, arr):
        # code here
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1

        prefix_sum = 0
        max_length = 0
        sum_index_map = {0: -1}  # Initialize with sum 0 at index -1
    
            prefix_sum += arr[i]
            if prefix_sum in sum_index_map:
                # Calculate the length of subarray with sum 0
                max_length = max(max_length, i - sum_index_map[prefix_sum])
            else:
                # Store the first occurrence of the prefix sum
                sum_index_map[prefix_sum] = i
        return max_length
...# } Driver Code Ends