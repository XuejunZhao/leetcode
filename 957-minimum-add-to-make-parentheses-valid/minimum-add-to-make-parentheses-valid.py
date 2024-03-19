class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        rights = []
        brankets = {'(':')'}
        for c in s: 
            if c == '(':
                stack.append('(')
            if c  == ')':    
                if stack: 
                    stack.pop(-1)
                else: 
                    rights.append(')')
        return len(stack)+len(rights)