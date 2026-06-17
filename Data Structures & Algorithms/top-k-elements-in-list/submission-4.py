class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1

        arr=[]
        for i,j in hm.items():
            arr.append([i,j])
        
        arr.sort()
        result=[]
        while k>len(result):
            result.append(arr.pop())

        return result