#User function Template for python3
import itertools

class Solution:
    def findPermutation(self, s):
        return list(set([''.join(p) for p in itertools.permutations(s)]))
        
...# } Driver Code Ends