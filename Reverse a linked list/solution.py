#function Template for python3

"""
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        Next = head
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev
...# } Driver Code Ends