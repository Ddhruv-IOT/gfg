
class Solution:
    def countPairs (self, arr, target) : 
        n = len(arr)
        i, j = 0, n - 1
        count = 0
        
        while i < j:
            current_sum = arr[i] + arr[j]
            
            if current_sum == target:
                if arr[i] == arr[j]:
                    # Special case: all elements between i and j are the same
                    count += (j - i) * (j - i + 1) // 2
                    break
                else:
                    # Count occurrences of arr[i] and arr[j]
                    count_i, count_j = 1, 1
                    while i + 1 < j and arr[i] == arr[i + 1]:
                        count_i += 1
                        i += 1
                    while j - 1 > i and arr[j] == arr[j - 1]:
                        count_j += 1
                        j -= 1
                    
                    count += count_i * count_j
                    i += 1
                    j -= 1
            elif current_sum < target:
                i += 1
            else:
                j -= 1
#User function Template for python3
        return count
...# } Driver Code Ends