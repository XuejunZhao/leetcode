class Solution:
    
    def removeDuplicateLetters(self, s: str) -> str:
        count_s = defaultdict(int)
        
        for c in s:
            count_s[ord(c)] = 1+count_s.get(ord(c), 0)
        res = []
        for i,c in enumerate(s):
            count_s[ord(c)] -= 1
            if c in res:
                continue
            # print (count_s)
            # print (res)
            while res and ord(res[-1]) >= ord(c) and count_s[ord(res[-1])] >= 1: 
                res.pop(-1)
            
            res.append(c)
            
            
        return ''.join(res)

        