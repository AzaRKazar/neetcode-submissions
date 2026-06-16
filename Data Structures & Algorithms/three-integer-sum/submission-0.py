class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute
        # n=len(nums)
        # output=[]
        # seen=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 triplets=tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 if triplets not in seen:
        #                     seen.add(triplets)
        #                     output.append(list(triplets))
                         
        
        # return output
        #optimal

        nums=sorted(nums)
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
         
            while left<right:
                total= nums[i]+nums[left]+nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                
                else:
                    res.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    right-=1
                    left+=1
        return res
