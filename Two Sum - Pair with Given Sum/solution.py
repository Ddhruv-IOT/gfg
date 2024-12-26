#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        seen = set()  # Using a set for constant time lookup
        for num in arr:
            complement = target - num
            if complement in seen:
                return True
            seen.add(num)
        return False

...# } Driver Code Ends