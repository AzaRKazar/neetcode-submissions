class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,column=len(matrix),len(matrix[0])
        left,right=0,row*column-1
        while left<=right:
            mid=(left+right)//2
            r=mid//column
            c=mid%column
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                left=mid+1
            else:
                right=mid-1
        return False
               