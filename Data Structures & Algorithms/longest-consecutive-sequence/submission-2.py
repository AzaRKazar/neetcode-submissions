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

        # nums.sort() 
        # longest=1
        # current=1
        # for i in range(len(nums)):
        #     if nums[i]==nums[i-1]+1:
        #         current+=1
        #     elif nums[i]==nums[i-1]:
        #         continue
        #     else:
        #         current=1
        #     longest=max(longest,current)
        # return longest
                

        num_set=set(nums)
        longest=0
        for n in nums:
            if n-1 not in num_set:
                length=1
                while n+length in num_set:
                    length+=1
                longest=max(longest,length)
        return longest