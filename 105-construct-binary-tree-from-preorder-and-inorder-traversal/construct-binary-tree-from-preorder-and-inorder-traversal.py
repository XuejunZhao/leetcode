# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: 
            return None 
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        left_length = root_idx 
        
        
        root.left = self.buildTree(preorder[1:1+left_length],inorder[:root_idx])
        root.right = self.buildTree(preorder[1+left_length:],inorder[root_idx+1:])
        return root
        