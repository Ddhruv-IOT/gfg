class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        curr=head
        prev=None
        tempTail=None
        tempHead=head
        n=0
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            n+=1
            if n%k==0 or curr==None:
                if tempTail:
                    tempTail.next=prev
                else:
                    head=prev
                prev=None
                tempTail=tempHead
                tempHead=curr
        return head

...# } Driver Code Ends
"""Node is defined as