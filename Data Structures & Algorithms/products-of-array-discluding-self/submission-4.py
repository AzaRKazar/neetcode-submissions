class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=n*[1]
        prefix=1
        for i in range(n):
            left[i]=prefix
            prefix*=nums[i]
        

        right=n*[1]
        suffix=1
        for i in range (n-1,-1,-1):
            right[i]=suffix
            suffix*=nums[i]


        output = n*[1]    
        for i in range(n):
            output[i]=left[i]*right[i]
        
        return output