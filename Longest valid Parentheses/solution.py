# User function Template for Python3

class Solution:
    def maxLength(self, s):
        # Stack to store the indices of the parentheses
        stack = [-1]  # Initialize with -1 to handle the base case
        max_len = 0   # Variable to store the maximum length of valid parentheses
    
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of the opening parenthesis onto the stack
                stack.append(i)
            else:
                # Pop the top of the stack when encountering a closing parenthesis
                stack.pop()
                # If the stack is not empty, calculate the length of the current valid substring
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    # If the stack is empty, push the current index as the new base
                    stack.append(i)
        return max_len
...# } Driver Code Ends