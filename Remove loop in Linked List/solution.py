    
        slow = head
        fast = head
        # Step 1: Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Loop detected
                break
        else:
            return  # No loop detected
        # Step 2: Find the starting node of the loop
        
        while slow != fast:
            fast = fast.next
        # Step 3: Remove the loop
        # Find the node before the starting node of the loop
        while fast.next != slow:
        # Break the loop
        fast.next = None

...# } Driver Code Ends
'''
# node class:
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return