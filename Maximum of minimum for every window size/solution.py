
class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        nser = []
        stack = []
       
        for i in reversed(range(n)):
            while stack and stack[-1][0]>=arr[i]:
                stack.pop()
            if stack:
                nser.append(stack[-1][1])
            else:
                nser.append(n)
            stack.append((arr[i],i))
        nser.reverse()
        nsel = []
        
        for i in range(n):
                nsel.append(stack[-1][1])
                nsel.append(-1)
        result = [0]*n
        # print(nser,nsel)
            ai = nser[i]-nsel[i]-2
            # print(ai,arr[i])
            result[ai] = max(result[ai],arr[i])
        for i in reversed(range(1,n)):
            result[i-1] = max(result[i],result[i-1])
        return result
...# } Driver Code Ends