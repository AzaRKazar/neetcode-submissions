# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0

        def helper(node,max_so_far):
            if node is None:
                return []
            if node.val >= max_so_far:
                max_so_far=max(max_so_far,node.val)
                self.count+=1
            helper(node.left,max_so_far)
            helper(node.right,max_so_far)


        helper(root,float('-inf'))    
        return self.count
        