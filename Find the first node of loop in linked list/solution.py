    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        #code here
        if not head or not head.next:
            return None
    
        slow, fast = head, head
        # Detect loop using Floyd's algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Loop detected
            if slow == fast:
                # Find the start of the loop
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        # No loop
        return None

...# } Driver Code Ends
#User function Template for python3
""" Node Class