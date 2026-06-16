class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq={}
        # for i in nums:
        #     freq[i]=freq.get(i,0)+1
        
        # sorted_items=sorted(freq.items(),reverse=True,key=lambda x:x[1])
        # return ([key for key,value in sorted_items[:k]])

        import heapq
        freq = {}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        heap=[]
        for key,value in freq.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [key for value,key in heap]
        freq = {}
        # for i in nums:
        #     freq[i] = freq.get(i, 0) + 1
    
        # heap = []
        # for num, count in freq.items():
        #     heapq.heappush(heap, (count, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
    
        # return [num for count, num in heap]
