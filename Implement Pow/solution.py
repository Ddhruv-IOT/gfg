...# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        res = 1
        base = b
        exponent = abs(e)
        
        while exponent > 0:
            if exponent % 2 == 1:
                res *= base
            base *= base
            exponent //=2
        return res if e >= 0 else 1 / res
