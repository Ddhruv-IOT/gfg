
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            height = min(arr[left], arr[right])
            width = right - left
            current_area = height * width
            
            # Update maximum area
            max_area = max(max_area, current_area)
            # Move the pointer pointing to the smaller height
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return max_area
...# } Driver Code Ends