class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        # for x,y in points:
        #     dist=x*x+y*y
        #     heapq.heappush(minHeap,(dist,[x,y]))
        # result=[]
        # for i in range(k):
        #     pop=heapq.heappop(minHeap)
        #     result.append(pop[1])

        # return result
        maxHeap=[]
        for x,y in points:
            dist=x*x+y*y
            heapq.heappush(maxHeap,(-dist,[x,y]))

            while len(maxHeap)>k:
                heapq.heappop(maxHeap)
            
        return [point for dist,point in maxHeap]