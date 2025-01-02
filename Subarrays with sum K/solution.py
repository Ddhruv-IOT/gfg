#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        cumulative_sum_map = {0: 1}  # We consider the sum 0 having 1 frequency (for subarrays starting from index 0)
        cumulative_sum = 0
        count = 0
    
        for num in arr:
            cumulative_sum += num
            # If (cumulative_sum - k) is found in the map, we found a subarray summing to k
            if cumulative_sum - k in cumulative_sum_map:
                count += cumulative_sum_map[cumulative_sum - k]
            # Store/update the frequency of the cumulative sum
            if cumulative_sum in cumulative_sum_map:
                cumulative_sum_map[cumulative_sum] += 1
            else:
                cumulative_sum_map[cumulative_sum] = 1
        return count
...# } Driver Code Ends