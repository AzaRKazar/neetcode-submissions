class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        stack=[0]
        maxarea=0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx=stack.pop()
                width=i-stack[-1]-1
                area=width*heights[idx]
                maxarea=max(area,maxarea)

            stack.append(i)
        return maxarea