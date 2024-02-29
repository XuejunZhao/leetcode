# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0 
        depth = 0
        res = [root]
        while res: 
            n = len(res)
            for i in range(n):
                curr = res.pop(0)
                if curr.left: 
                    res.append(curr.left)
                if curr.right:
                    res.append(curr.right)
            depth += 1
        return depth