#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def boundaryTraversal(self, root):
        # Code here
        li=[]
        if not self.leaf(root): li.append(root.data)
        self.leftSide(root,li)
        self.bottom(root,li)
        self.rightSide(root,li)
        return li
        
    def leftSide(self,node,li):
        curr=node.left
        while curr:
            if not self.leaf(curr): li.append(curr.data)
            if not curr.left: curr=curr.right
            else: curr=curr.left
            
    def bottom(self,node,li):
        if not node: return 
        if self.leaf(node):
            li.append(node.data)
            return 
        self.bottom(node.left,li)
        self.bottom(node.right,li)
    def rightSide(self,node,li):
        curr=node.right
        revIdx=len(li)
            if not curr.right: curr=curr.left
            else: curr=curr.right
        li[revIdx:]=reversed(li[revIdx:])
    
    def leaf(self,node):
        return not node.left and not node.right
...# } Driver Code Ends