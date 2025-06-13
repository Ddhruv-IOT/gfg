#User function Template for python3

import math
class Solution:
    def kokoEat(self,arr,k):
        l, r = 1, max(arr)
        while l < r:
            m = (l + r) // 2
            if sum([math.ceil(v/m) for v in arr]) <= k:
                r = m
            else:
                l = m + 1
        return l