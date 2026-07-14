class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-i for i in stones]
        heapq.heapify(max_heap)

        while len(max_heap)!=1 and len(max_heap)!= 0 :
            pop1 = -(heapq.heappop(max_heap))
            pop2 = -(heapq.heappop(max_heap))
            if pop1!=pop2:
                diff_pop=abs(pop1-pop2)
                heapq.heappush(max_heap,-diff_pop)
            
        return -(max_heap[0]) if len(max_heap)==1 else 0


