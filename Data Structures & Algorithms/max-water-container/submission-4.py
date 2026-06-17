class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        # brute
        # area=[]
        # for i in range(n):
        #     diff=0
        #     for j in range(i+1,n):
        #         diff=abs(i-j)
        #         height=min(heights[i],heights[j])
        #         area.append(diff*height)
        # return (max(area))

        # left = 0
        # right=n-1
        # max_area=0
        # while left<right:
        #     if heights[left]<heights[right]:
        #         area=(right-left)*(heights[left])
        #         max_area = max(max_area, area)
        #         left+=1
        #     elif heights[right]<heights[left]:
        #         area=(right-left)*(heights[right])
        #         max_area = max(max_area, area)
        #         right-=1
        #     else:
        #         area = (right - left) * heights[left]
        #         max_area = max(max_area, area)
        #         left += 1
        #         right -= 1
        # return max_area














        i=0
        maxi=0
        j=len(heights)-1
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            area=width*height
            maxi=max(area,maxi)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return maxi













