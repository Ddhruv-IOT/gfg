...# } Driver Code Ends
#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        freq = {}
        count = 0
    
        for num in arr:
            # Calculate the complement
            complement = target - num
            
            # If the complement exists in the dictionary, add its count to the pair count
            if complement in freq:
                count += freq[complement]
            # Update the frequency dictionary for the current number
            freq[num] = freq.get(num, 0) + 1
        
        return count