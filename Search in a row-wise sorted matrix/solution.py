class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	def search(arr, x):
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                
                # If x == mid, return true
                if x == arr[mid]:
                    return True
                
                # If x < arr[mid], search in the left half
                if x < arr[mid]:
                    hi = mid - 1
                
                # If x > arr[mid], search in the right half
                else:
                    lo = mid + 1
            return False

        n, m = len(mat), len(mat[0])
    
        # Iterate over all the rows to find x
        for i in range(n):
            
            # Perform binary search on the ith row
            if search(mat[i], x):
                return True
    
        # If x was not found, return false
        return False
