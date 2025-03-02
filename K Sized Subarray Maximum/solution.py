#User function Template for python3
from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self,arr,k):
        n = len(arr)
        # Deque to store indices of array elements
        dq = deque()
        result = []
        # Process the first window of size k
        for i in range(k):
            # Remove elements that are smaller than the current element
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            # Add the current element at the back of the deque
            dq.append(i)
        
        # Process the remaining elements
        for i in range(k, n):
            # The front of the deque is the max of the previous window
            result.append(arr[dq[0]])
            # Remove elements which are out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
        # Add the maximum of the last window
        result.append(arr[dq[0]])
        return result
...# } Driver Code Ends