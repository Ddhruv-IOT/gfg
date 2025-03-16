#User function Template for python3
class Solution:
    def minJumps(self, arr):
        #code here
        n = len(arr)
    
        if n <= 1:
            return 0  # If array has only one element, no jumps are needed
        
        if arr[0] == 0:
            return -1  # If the first element is 0, we can't move anywhere
        jumps = 0
        farthest = 0
        current_end = 0
        for i in range(n - 1):
            farthest = max(farthest, i + arr[i])  # Update the farthest point reachable
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:  # If we've reached or surpassed the last index
                    return jumps
        return -1  # If we finish the loop without reaching the end
