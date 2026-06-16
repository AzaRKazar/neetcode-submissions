class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #burtal
        # temp=temperatures
        # result=[0]*len(temp)
        # for i in range(0,len(temp)):
        #     for j in range(i+1,len(temp)):
        #         if temp[i]<temp[j] :
        #             result[i]=j-i
        #             break
        # return result

        #our stack tuples are (temp, index) — not (index, temp)
                
        #left to right stack
        temp=temperatures
        res=[0]*len(temp)
        stack=[]
        # for i,t in enumerate(temp):
        #     while stack and stack[-1][0]<t:
        #         t_stack,i_stack=stack.pop()
        #         res[i_stack]=i-i_stack
        #     stack.append((t,i))
        # return res

        #right to left:
        for i in range(len(temp)-1,-1,-1):
            while stack and temp[i]>=temp[stack[-1]]:
                stack.pop()
            if stack:
                res[i]=stack[-1]-i
            stack.append(i)
        return res