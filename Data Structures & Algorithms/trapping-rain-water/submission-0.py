class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        prefix=0
        for i in range(0,len(height)):
            prefix=max(prefix,height[i])
            leftmax[i]=prefix
        suffix=0
        rightmax=[0]*len(height)
        for i in range(len(height)-1,-1,-1):
            suffix=max(suffix,height[i])
            rightmax[i]=suffix
        water=[0]*len(height)
        for i in range(len(height)):
            water[i]=max(leftmax[i],rightmax[i])-height[i]

        return sum(water)

