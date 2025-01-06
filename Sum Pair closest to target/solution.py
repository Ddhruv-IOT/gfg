    
        # Initialize variables
        closest_sum = float('inf')
        best_pair = []
        max_abs_diff = -1
        # Two-pointer approach
        left, right = 0, len(arr) - 1
        while left < right:
            a, b = arr[left], arr[right]
            current_sum = a + b
            # Update closest pair if better found
            if abs(current_sum - target) < abs(closest_sum - target) or \
               (abs(current_sum - target) == abs(closest_sum - target) and abs(b - a) > max_abs_diff):
                closest_sum = current_sum
                best_pair = [a, b]
                max_abs_diff = abs(b - a)
            # Move pointers
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return best_pair

...# } Driver Code Ends
#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr) < 2:
            return []
        # Sort the array
        arr.sort()