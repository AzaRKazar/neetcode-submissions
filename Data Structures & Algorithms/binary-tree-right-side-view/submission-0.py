# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        result=[]
        que=deque([root])
        while que:
            levelsize=len(que)
            for i in range(levelsize):
                node=que.popleft()
                
                if i==levelsize-1:
                    result.append(node.val)
                
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)

        return result