...# } Driver Code Ends

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    # Return the kth smallest element in the given BST 
    def inorder(self, root, k, count, result):
        #code here.
        if root is None or result[0] != -1:
            return
        
        # Left subtree
        self.inorder(root.left, k, count, result)
        # Process current node
        count[0] += 1
        if count[0] == k:
            result[0] = root.data
        # Right subtree
        self.inorder(root.right, k, count, result)
    # Return the kth smallest element in the given BST
    def kthSmallest(self, root, k):
        count = [0]
        result = [-1]
        self.inorder(root, k, count, result)
        return result[0]