# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder:
        #     return None
       
        # root_val=preorder[0]
        # root=TreeNode(root_val)


        # # find inorder
        # mid=inorder.index(root_val)
        # in_left=inorder[:mid]
        # in_right=inorder[mid+1:]

        # # fine preorder
        # pre_left=preorder[1:len(in_left)+1]
        # pre_right=preorder[len(in_left)+1:]

        # root.left=self.buildTree(pre_left,in_left)
        # root.right=self.buildTree(pre_right,in_right)
        # return root


        dicti={val:idx for idx,val in enumerate(inorder)}
        self.pre_idx=0

        def helper(left,right):
            if left>right:
                return None
            rootval=preorder[self.pre_idx]
            self.pre_idx+=1
            root=TreeNode(rootval)

            mid=dicti[rootval]

            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)

            return root
        return helper(0,len(inorder)-1)

