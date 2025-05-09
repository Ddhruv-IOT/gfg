...# } Driver Code Ends

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def findTarget(self, root, target): 
        # your code here.
        s = set()
        
        def fun(root):
            if root == None:
                return False
            if target - root.data in s:
                return True
                
            s.add(root.data)
            
            return fun(root.left) or fun(root.right)
        return fun(root)