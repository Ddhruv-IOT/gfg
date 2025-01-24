#User function Template for python3
'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next         # Move slow pointer one step
            fast = fast.next.next    # Move fast pointer two steps
            # If slow and fast meet, a cycle exists
            if slow == fast:
                return True
        # If we exit the loop, no cycle exists
        return False
...# } Driver Code Ends