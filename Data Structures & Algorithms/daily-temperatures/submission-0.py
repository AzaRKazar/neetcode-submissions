class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        result=[0]*len(temp)
        for i in range(0,len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i]<temp[j] :
                    result[i]=j-i
                    break
        return result
                

