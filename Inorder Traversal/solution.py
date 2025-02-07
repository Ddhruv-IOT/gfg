
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def inOrder(self,root):
        arr = []
        if root:
            arr += self.inOrder(root.left)
            arr.append(root.data)
            arr += self.inOrder(root.right)
        return arr
...# } Driver Code Ends