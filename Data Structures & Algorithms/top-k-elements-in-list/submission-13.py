class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1

        arr=[]
        for key,value in hm.items():
            arr.append([value,key])
        
        arr.sort(-1)
        # result=[]
        # while k>len(result):
        #     result.append(arr.pop()[1])
        return arr[:k]