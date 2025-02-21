
class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
    
        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map.keys():  # If it's a closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        return not stack  
...# } Driver Code Ends