    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        dummy = Node(-1)
        current = dummy
        
        # Traverse both lists
        while head1 and head2:
            if head1.data < head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
    
        # Attach remaining nodes
        if head1:
            current.next = head1
        if head2:
            current.next = head2
        return dummy.next
...# } Driver Code Ends
#User function Template for python3
# Node Class
class Node: