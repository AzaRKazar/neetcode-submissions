# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def SameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        if p.val!=q.val:
            return False
        
        return self.SameTree(p.left,q.left) and self.SameTree(p.right,q.right)
    
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False
        
        match=self.SameTree(root,subRoot)
        matchl=self.isSubtree(root.left,subRoot)
        matchr=self.isSubtree(root.right,subRoot)

        if match or matchl or matchr:
            return True
        else:
            return False

            
            
