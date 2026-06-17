class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i]==nums[j]:
                    return True

        return False