"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect2nodes(self, left: 'Optional[Node]', right: 'Optional[Node]') -> 'Optional[Node]':
        if not left: return right 
        if not right: return left 
        left.next = right
        return left, right

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: 
            return root
        left = root.left
        right = root.right
        self.connect2nodes(left,right)

        if root.next != None and right: 
            self.connect2nodes(right, root.next.left)
        self.connect(left)
        self.connect(right)
        
        return root