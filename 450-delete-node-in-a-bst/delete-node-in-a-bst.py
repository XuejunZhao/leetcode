# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: 
            return None 
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            curr = root.right 
            
            while curr.left: 
                curr = curr.left 
           
            
            root.right = self.deleteNode(root.right, curr.val)
            curr.left = root.left
            curr.right = root.right
            root = curr
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: 
            root.left = self.deleteNode(root.left, key)
        return root 

        