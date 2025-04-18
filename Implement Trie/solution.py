#User function Template for python3
class Node:
    
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False

class Trie:
        self.root=Node()
    def insert(self, word: str):
        curr=self.root
        for w in word:
            i=ord(w)-ord("a")
            if curr.children[i]==None:
                curr.children[i]=Node()
            curr=curr.children[i]
        curr.isEnd=True
    def search(self, word: str) -> bool:
                return False
        return curr.isEnd
    def isPrefix(self, word: str) -> bool:
        return True
...# } Driver Code Ends