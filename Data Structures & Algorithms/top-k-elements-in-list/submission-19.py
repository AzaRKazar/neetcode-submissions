class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hm={}
        # for i in nums:
        #     hm[i]=hm.get(i,0)+1

        # arr=[]
        # for key,value in hm.items():
        #     arr.append([value,key])
        
        # arr.sort(reverse=True)
        # # result=[]
        # # while k>len(result):
        # #     result.append(arr.pop()[1])
        # return  [i[1] for i in arr[:k]]


        # optimal solution
        hm={}
        for i in nums:
            hm[nums]=hm.get(nums,0)+1
        buckets=[[] for i in range(len(nums)+1)]

        for key,value in hm.items():
            buckets[value].append(key)
        result=[]
        for i in range(len(buckets)-1,0,-1):
            for j in range(buckets[i]):
                result.append(num)
            if len(result)==k:
                return result
