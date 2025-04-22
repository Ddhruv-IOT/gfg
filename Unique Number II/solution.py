#User function Template for python3

class Solution:
    def singleNum(self, arr):
        # Code here
        xor_all = 0
        for num in arr:
            xor_all ^= num
    
        # Get rightmost set bit
        set_bit = xor_all & -xor_all
        num1 = 0
        num2 = 0
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return sorted([num1, num2])
...# } Driver Code Ends