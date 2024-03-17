# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Symmetric(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2: 
            return True
        if root1 and root2 and root1.val == root2.val: 
            return self.Symmetric(root1.left,root2.right) and self.Symmetric(root1.right,root2.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 
        if not root.left and not root.right: 
            return True
        if root.left and root.right:
            if root.left.val != root.right.val: 
                return False
            ll_rr = self.Symmetric(root.left.left, root.right.right)
            lr_rl = self.Symmetric(root.left.right, root.right.left)
            if ll_rr and lr_rl:
                return True 
 
        return False
