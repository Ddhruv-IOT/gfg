class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        
class Solution:
    def levelOrder(self, root):
        # Your code here
        if not root:
            return []
            
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)  # Store level-wise nodes
    
        return result

...# } Driver Code Ends