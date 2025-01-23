#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
class Solution:
    def cloneLinkedList(self, head):
        curr=head
        while curr:
            temp=Node(curr.data)
            temp.next=curr.next
            curr.next=temp
            curr=temp.next
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next
        newHead=curr.next
            temp=curr.next
            curr.next=temp.next
            if curr:
                temp.next=curr.next
        return newHead
    
...# } Driver Code Ends