#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    #Function to find the height of a binary tree.
    def height(self, node):
        
        if node is None:
            return -1
        else:
            return max(self.height(node.left),self.height(node.right)) +1
...# } Driver Code Ends