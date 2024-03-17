# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.target = 0
    def dfs(self, root):
        if root:
            self.track.append(root.val)
            if not root.left and not root.right:
                if sum(self.track) == self.target: 
                    self.res.append(self.track[:])
                
                    
            elif root.left or root.right:
                
                self.dfs(root.left)
                
                self.dfs(root.right)
            self.track.pop(-1)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: 
            return []
        
        self.target = targetSum
        self.dfs(root)
        return self.res
        