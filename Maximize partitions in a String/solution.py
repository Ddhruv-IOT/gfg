class Solution:
    def maxPartitions(self, s: str) -> int:
        last_occurrence = {ch: i for i, ch in enumerate(s)}  # Store last index of each character
        partitions = 0
        end = 0
    
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])  # Expand the partition boundary
            if i == end:  # Found a valid partition
                partitions += 1
        return partitions

...# } Driver Code Ends