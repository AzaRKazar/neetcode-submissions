# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def MaxDepth(node):
            if node is None:
                return 0
            left=MaxDepth(node.left)
            right=MaxDepth(node.right)
            self.diameter=max(left+right,self.diameter)
            return 1+max(left,right)

        MaxDepth(root)
        return self.diameter
            