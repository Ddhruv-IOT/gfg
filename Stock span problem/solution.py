...# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        #write code here
        n=len(arr)
        ans=[]
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            ans.append(i-stack[-1] if stack else i+1)
            stack.append(i)
        return ans
        