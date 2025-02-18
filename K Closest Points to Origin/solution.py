...# } Driver Code Ends

import heapq
class Solution:
    def kClosest(self, points, k):
        heap=[]
        for point in points:
            dist=point[0]**2+point[1]**2
            if len(heap)<k:
                heapq.heappush(heap,(-dist,point))
            else:
                if -dist>heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist,point))
        return [point for _,point in heap]
        