#User function Template for python3
from collections import defaultdict

class Solution:
    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        
        # Dictionary to store groups of anagrams
        anagram_groups = defaultdict(list)
        # Group words by their sorted version
        for word in arr:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    
        # Return groups in the order of their first appearance
        result = [anagram_groups[sorted_word] for sorted_word in anagram_groups.keys()]
        return result
        #code here
...# } Driver Code Ends