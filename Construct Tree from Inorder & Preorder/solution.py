#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        
        index_map = { inorder[i] : i for i in range(len(inorder)) }
        pre_inx = 0
        def construct(left , right):
            nonlocal pre_inx
            if left> right:
                return None
            
            val = preorder[pre_inx]
            pre_inx+=1
            inorder_inx = index_map[val]
            root = Node(val)
            root.left = construct(left , inorder_inx-1)
            root.right = construct(inorder_inx+1,right)
            return root            
        return construct(0,len(inorder)-1)
...# } Driver Code Ends