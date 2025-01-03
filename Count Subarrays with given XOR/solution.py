class Solution:
    def subarrayXor(self, arr, k):
        # code here
        freq = {0: 1}  # To handle the case when subarray itself has XOR equal to k
        prefixXOR = 0
        count = 0
        
        for num in arr:
            prefixXOR ^= num  # Update prefix XOR
            targetXOR = prefixXOR ^ k
            
            # If prefixXOR ^ k exists in freq, it means there are subarrays with XOR = k
            count += freq.get(targetXOR, 0)
            # Update the frequency of prefixXOR in the hashmap
            freq[prefixXOR] = freq.get(prefixXOR, 0) + 1
        return count

...# } Driver Code Ends