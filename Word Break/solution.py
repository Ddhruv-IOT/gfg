class Solution:
    def wordBreak(self, s, dictionary):
        maxLen=max(len(item) for item in dictionary)
        words=set(dictionary)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            end=max(-1,i-1-maxLen)
            for j in range(i-1,end,-1):
                if dp[j] and s[j:i] in words:
                    dp[i]=True
                    break
        return dp[n]

...# } Driver Code Ends