"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root 
        curr = root 
        res = [curr]
        while res: 
            n = len(res)
            # print (n)
            for i in range(n-1):
                res[i].next = res[i+1]
            for i in range(n):
                curr = res.pop(0)

                if curr.left: 
                    res.append(curr.left)
                if curr.right: 
                    res.append(curr.right)
     
        return root

