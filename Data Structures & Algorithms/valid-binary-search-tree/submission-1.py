# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low=float("-inf")
        high=float("inf")
        def helper(node,low,high):
            if node is None:
                return True
            if low>=node.val or high<=node.val:
                return False
            left=helper(node.left,low,node.val)
            right=helper(node.right,node.val,high)

            return left and right
            
        
        return helper(root,low,high)