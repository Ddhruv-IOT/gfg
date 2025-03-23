#User function Template for python3
class Solution:
    def countWays(self, digits):
        # Code here
        if not digits or digits[0] == '0':  # Invalid case
            return 0

        # HashMap for reference (not directly needed for decoding)
        mapping = {str(i): chr(64 + i) for i in range(1, 27)}
    
        prev2, prev1 = 1, 1  # Base cases for empty string and single char
        for i in range(1, len(digits)):
            current = 0
            
            # Check single-digit mapping
            if digits[i] != '0':  # '0' cannot be decoded alone
                current += prev1
            # Check two-digit mapping
            if 10 <= int(digits[i-1:i+1]) <= 26:
                current += prev2
            prev2, prev1 = prev1, current  # Move pointers
        return prev1
...# } Driver Code Ends