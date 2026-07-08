# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values=[]
        def helper(node):
            if node is None:
                return 
            helper(node.left)
            self.values.append(node.val)
            helper(node.right)

        helper(root)
        return self.values[k-1]