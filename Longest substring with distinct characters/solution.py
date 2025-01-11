#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        start = 0
        max_len = 0
        char_set = set()
        
        # Iterate over the string with the end pointer
        for end in range(len(s)):
            # If character at s[end] is in the set, move the start pointer
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            # Add the current character to the set
            char_set.add(s[end])
            # Update the maximum length of the substring
            max_len = max(max_len, end - start + 1)
        return max_len
...# } Driver Code Ends