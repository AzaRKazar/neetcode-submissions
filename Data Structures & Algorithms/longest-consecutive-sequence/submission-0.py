class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest=0
        # for i in range(len(nums)):
        #     length=1
        #     current=nums[i]

        #     while current +1 in nums:
        #         length+=1
        #         current+=1
            
        #     longest=max(longest,length)
        # return longest

        nums.sort()
        for i in range(len(nums)):
            current=i
           
            while nums[i]==nums[i]+1:
                longest+=1
            longest=max(0,longest)

                
