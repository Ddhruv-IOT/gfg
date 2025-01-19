# Your task is to complete this function

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    
    def rotate(self, head, k):
        # Edge case: if head is None or k is 0
        if not head or k == 0:
            return head
        
        # Step 1: Determine the length of the linked list
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1
        # Normalize k if k is greater than length
        k = k % length
        # If k is 0 after normalization, return the head
        if k == 0:
        # Step 2: Find the (k+1)th node
        for _ in range(k - 1):
        # Step 3: Set the new head and new tail
        new_head = current.next
        current.next = None
        # Step 4: Find the old tail and connect it to the old head
        old_tail = new_head
        while old_tail.next:
            old_tail = old_tail.next
        old_tail.next = head
        return new_head
...# } Driver Code Ends